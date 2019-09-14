import logging

import zmq as orig_zmq
from gevent.coros import Semaphore

from pylib import disk, conf, timing, textual, benchmarker
from pylib import disk, conf, timing, textual
from pylib.metric.benchmarker import Benchmarker
from pylib.wiring import forming

log = logging.getLogger(__name__)

DEFAULT_QUEUE_SIZE = 10000

PRINTERS = {
    "speed_freq": timing.speed_printer,
    "exit_freq": timing.exit_printer,
}

BENCHMARKER = None

import zmq.green as gevent_zmq

def Wire(section, conf_path=None, use_gevent=False, zmq_context=None,
        repo_name=None):
    debug_name = section
    if repo_name is not None:
        debug_name = "%s[%s]" % (debug_name, repo_name)
    if zmq_context is None:
        zmq = orig_zmq
        if use_gevent:
            from pylib.wiring import gevent_zmq as zmq
        log.info("wire %s; creating new ZeroMQ context", debug_name)
        zmq_context = zmq.Context()

    config = _get_config(conf_path, repo_name, section=section)
    options = _get_section(config, section)

    return _Wire(zmq_context, options, debug_name)


def create_wire(zmq_context, options):
    return _Wire(zmq_context, options)


class _Wire(object):
    """A configured ZeroMQ socket.
    Supported options:
        socket ... a ZeroMQ address (e.g., PULL:bind:tcp://127.0.0.1:5502).
        identifier ... a ZeroMQ identity. Receivers should use it.
        queue_size ... the HWM option for senders (default=10000).
        format ... a serialization format to use (default=None).
        speed_freq ... print the rate of received messages.
        exit_freq ... exit the app after the given number of received msgs.
    """

    def __init__(self, zmq_context, options, debug_name=None):
        if debug_name is None:
            debug_name = options["socket"]
        self.debug_name = debug_name
        log.debug('wire %s; initializing', self.debug_name)

        socket_info = options["socket"]
        identifier = options.get("identifier")
        queue_size = int(options.get("queue_size", DEFAULT_QUEUE_SIZE))
        self.coder = forming.get_coder(options.get("format"))

        socket_type, address = socket_info.split(':', 1)
        if socket_type == "XREQ":
            socket_type = "DEALER"
        elif socket_type == "XREP":
            socket_type = "ROUTER"
        self.socket_type = socket_type

        zmq = orig_zmq
        # create socket of given type, PUB/SUB/PUSH/PULL
        self.socket = zmq_context.socket(getattr(zmq, socket_type))

        self.socket.setsockopt(zmq.SNDHWM, queue_size)
        self.socket.setsockopt(zmq.RCVHWM, queue_size)

        if identifier:
            self.socket.setsockopt(zmq.IDENTITY, textual.utf8(identifier))

        if socket_type == 'SUB':
            self.socket.setsockopt(zmq.SUBSCRIBE, '')

        self.send_multipart_semaphore = Semaphore()
        self._decorate_recv(options)
        _connect(self.socket, address)

        #benchmarker
        self._benchmarker =None

    def _decorate_recv(self, options):
        aspects = []
        for name, printer in PRINTERS.iteritems():
            freq = options.get(name)
            if freq is not None:
                freq = int(freq)
                log.warn("wire %s; reporting %s every %s messages",
                        self.debug_name, name, freq)
                aspects.append(printer(freq).next)

        global BENCHMARKER
        if options.get('benchmarker'):
            time_freq = int(options.get('benchmarker'))
            if BENCHMARKER is None:
                BENCHMARKER = benchmarker.Benchmarker(time_freq)

            self.recv_raw = BENCHMARKER.wrap_recv(self.recv_raw)
            self.recv = BENCHMARKER.wrap_recv(self.recv)
            self.recv_multipart = BENCHMARKER.wrap_recv(self.recv_multipart)

            self.send_raw = BENCHMARKER.wrap_send(self.send_raw)
            self.send = BENCHMARKER.wrap_send(self.send)
            self.send_multipart = BENCHMARKER.wrap_send(self.send_multipart)
        self.benchmarker = BENCHMARKER

        if aspects:
            self.recv_raw = _append_aspects(self.recv_raw, aspects)
            self.recv = _append_aspects(self.recv, aspects)
            self.recv_multipart = _append_aspects(self.recv_multipart,
                    aspects)

            self.send_raw = _append_aspects(self.send_raw, aspects)
            self.send = _append_aspects(self.send, aspects)
            self.send_multipart = _append_aspects(self.send_multipart,
                    aspects)

    def start_benchmarker_processing(self):
        benchmarker = self.benchmarker
        if benchmarker:
            benchmarker.start_processing()

    def get_socket_type(self):
        return self.socket_type

    def send_raw_nb(self, message):
        log.debug("wire %s; sending raw msg; msg=%r", self.debug_name, message)
        if self._benchmarker:
            self._benchmarker.start_send()
        self.socket.send(message,orig_zmq.NOBLOCK)
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_raw(self, message):
        log.debug("wire %s; sending raw msg; msg=%r", self.debug_name, message)
        if self._benchmarker:
            self._benchmarker.start_send()
        self.socket.send(message)
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send(self, message):
        log.debug("wire %s; sending msg; msg=%r", self.debug_name, message)
        if self._benchmarker:
            self._benchmarker.start_send()
        self.socket.send(self.coder.dumps(message))
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_multipart_with_id(self, message):
        if self._benchmarker:
            self._benchmarker.start_send()
        with self.send_multipart_semaphore:
            #log.debug("wire %s; sending msg; msg=%r", self.debug_name, event)
            self.socket.send_multipart(message)

    def recv_multipart_with_id(self):
        if self._benchmarker:
            self._benchmarker.start_recv()
        parts = self.socket.recv_multipart()
        if self.coder is forming.NoneCoder:
            log.debug("wire %s; got msg; msg=%r", self.debug_name, parts)
            return parts

        identity, encoded = parts
        msg = self.coder.loads(encoded)
        log.debug("wire %s; got msg; msg=%r", self.debug_name, msg)
        if self._benchmarker:
            self._benchmarker.stop_recv()
        return identity, msg

    def send_multipart(self, message):
        if self._benchmarker:
            self._benchmarker.start_send()
        with self.send_multipart_semaphore:
            if self.coder is forming.NoneCoder:
                log.debug("wire %s; sending msg; msg=%r", self.debug_name, message)
                self.socket.send_multipart(message)
                return

            identity, event = message
            log.debug("wire %s; sending msg; msg=%r", self.debug_name, event)
            self.socket.send_multipart((identity, self.coder.dumps(event)))
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_with_norm_policy_and_repo(self, event):
        """
        """
        if self._benchmarker:
            self._benchmarker.start_send()

        self.send(event)

        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_with_prefix_nb(self, prefix, event):
        """
        """
        if self._benchmarker:
            self._benchmarker.start_send()
        self.send_raw_nb(prefix + "\n" + self.coder.dumps(event))
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_with_repo(self, repo, event):
        """
        """
        if self._benchmarker:
            self._benchmarker.start_send()
        self.send_raw(repo + "\n" + self.coder.dumps(event))
        if self._benchmarker:
            self._benchmarker.stop_send()

    def send_with_mid(self, message):
        """send message after serializing prepended by mid and newline.
        """
        if self._benchmarker:
            self._benchmarker.start_send()
        #assert self.coder is forming.MidMarshalCoder
        self.send(message)
        if self._benchmarker:
            self._benchmarker.stop_send()

    def recv_raw(self):
        if self._benchmarker:
            self._benchmarker.start_recv()
        msg = self.socket.recv()
        log.debug("wire %s; got raw msg; msg=%r", self.debug_name, msg)
        if self._benchmarker:
            self._benchmarker.stop_recv()
        return msg

    def recv(self):
        if self._benchmarker:
            self._benchmarker.start_recv()
        msg = self.coder.loads(self.socket.recv())
        log.debug("wire %s; got msg; msg=%r", self.debug_name, msg)
        if self._benchmarker:
            self._benchmarker.stop_recv()
        return msg

    def recv_multipart(self):
        if self._benchmarker:
            self._benchmarker.start_recv()
        parts = self.socket.recv_multipart()
        if self.coder is forming.NoneCoder:
            log.debug("wire %s; got msg; msg=%r", self.debug_name, parts)
            return parts

        identity, encoded = parts
        msg = self.coder.loads(encoded)
        log.debug("wire %s; got msg; msg=%r", self.debug_name, msg)
        if self._benchmarker:
            self._benchmarker.stop_recv()
        return identity, msg

    def recv_raw_with_mid(self):
        """returns tuple of mid and raw_data
        """
        if self._benchmarker:
            self._benchmarker.start_recv()
        #assert self.coder is forming.MidMarshalCoder
        raw = self.recv_raw()
        mid, encoded = raw.split("\n", 1)
        if self._benchmarker:
            self._benchmarker.stop_recv()
        return mid, encoded

    def close(self, immediate=False):
        if immediate:
            self.socket.setsockopt(orig_zmq.LINGER, 0)
        self.socket.close()

    def __str__(self):
        return "Wire(%s)" % self.debug_name

    def setBenchmarker(self,benchmarker):
        self._benchmarker=benchmarker


def _connect(socket, address):
    """Binds or connects the socket to the given address.
    Multiple addresses can be separated by comma (,).
    Example address:
        address = "bind:tcp://127.0.0.1:5504,bind:tcp://10.105.0.2:5504"
    """
    addresses = address.split(",")
    for socket_addr in addresses:
        method, protocol_addr = socket_addr.split(":", 1)
        try:
            getattr(socket, method)(protocol_addr)
        except Exception, e:
            log.error("wire; unable to connect; method=%s; addr=%s; error=%s",
                    method, protocol_addr, e)
            raise


def _get_config(config_or_path, repo_name, section=None):
    if config_or_path is None:
        config_or_path = disk.get_sibling(__file__, 'wiring.conf')

    if isinstance(config_or_path, basestring):
        config = conf.get_config(config_or_path)
    else:
        config = config_or_path

    if isinstance(repo_name, (tuple, list)):
        assert section, "'section' is required when repo_name is list or tuple"
        combined_socket = ''
        for repo in repo_name:
            config.set("DEFAULT", "repo_name", repo)
            socket = config.get(section, 'socket')
            if not combined_socket:
                combined_socket = socket
            else:
                combined_socket += ',%s' % socket.split(':', 1)[-1]

        config.set(section, 'socket', combined_socket)

    elif repo_name is not None:
        config.set("DEFAULT", "repo_name", repo_name)

    return config


def _get_section(config, section_name):
    options = {}
    for key in config.options(section_name):
        options[key] = config.get(section_name, key)

    return options


def _append_aspects(orig_func, aspects):
    def new_func(*args, **kw):
        result = orig_func(*args, **kw)
        for aspect in aspects:
            aspect()
        return result

    return new_func


# Used for experiments from python console.
def simple(socket, **kw):
    zmq_context = orig_zmq.Context()
    kw["socket"] = socket
    return create_wire(zmq_context, kw)


if __name__ == '__main__':
    from pylib import logger
    logger.configure(syslog=False)

    zmq_context = orig_zmq.Context()

    publisher = Wire('collector_out', zmq_context=zmq_context)
    subscriber = Wire('norm_front_in', zmq_context=zmq_context, repo_name='wiring')

    publisher.send('#mid=123#msg=hi')
    print subscriber.recv()  # prints 'hi'

    sender = create_wire(zmq_context, dict(
        socket='PUSH:connect:tcp://127.0.0.1:5678'))
    receiver = create_wire(zmq_context, dict(
        socket='PULL:bind:tcp://127.0.0.1:5678'))

    sender.send('create_wire() implemented')
    print receiver.recv()  # prints 'create_wire() implemented'
    receiver.close()

    sender = simple('PUSH:connect:tcp://127.0.0.1:5678', format="json")
    receiver = simple('PULL:connect:tcp://127.0.0.1:5677,bind:tcp://127.0.0.1:5678', format="json")

    sender.send('simple() implemented')
    print receiver.recv()  # prints 'simple() implemented'
