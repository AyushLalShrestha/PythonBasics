import sys
import zmq
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = "topic"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

total_value = 0
while True:
    response = socket.recv()
    print response
    # topic, messagedata = response.split()
    total_value += 1


