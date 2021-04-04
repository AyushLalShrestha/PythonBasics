import time
import zmq


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")

    # Start your result manager and workers before you start your producers
    for num in xrange(20000):
        json_message = dict(
            num=num,
            device="win IT Server",
            action="login" if num % 5 == 0 else "audit_log"
        )
        zmq_socket.send_json(json_message)
        print "sending {}".format(json_message)
        time.sleep(3)


producer()
