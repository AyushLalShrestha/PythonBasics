"""
zmq sockets are of certain types which enable one of the various communication patterns.
zmq socket type must be passed during socket creation.
"""
# ------------------------------------------------ pairserver.py ------------------------------------------------

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send("Server message to client3")
    msg = socket.recv()
    print msg
    time.sleep(1)


# ------------------------------------------------ pairclient.py ------------------------------------------------
import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print msg
    socket.send("client message to server1")
    socket.send("client message to server2")
    time.sleep(1)

# ------------------------------------------------ running it ------------------------------------------------

"""
python pairserver.py <port>
python pairclient.py <port>
"""