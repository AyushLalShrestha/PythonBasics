# ------------------------------------------------ reqrep_server.py ------------------------------------------------
import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)
    socket.send("World from %s" % port)


# ------------------------------------------------ reqrep_client.py ------------------------------------------------
# Provide two ports of two different servers to connect to simultaneously.
import zmq
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

# You have to send a request and then wait for reply
# Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send ("Hello")
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"


"""
Executing the scripts:
    python reqrep_server.py 5546
    python reqrep_server.py 5556
    python reqrep_client.py 5546 5556

Expected Output:
    Connecting to hello world server...
    Sending request  1 ...
    Received reply  1 [ World from 5556 ]
    Sending request  2 ...
    Received reply  2 [ World from 5546 ]
    Sending request  3 ...
    Received reply  3 [ World from 5556 ]
    Sending request  4 ...
    Received reply  4 [ World from 5546 ]
    Sending request  5 ...
    Received reply  5 [ World from 5556 ]
    Sending request  6 ...

"""