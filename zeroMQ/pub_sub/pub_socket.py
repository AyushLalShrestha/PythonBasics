
import zmq
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))

message_count = 1
while True:
    socket.send("{} {} x Some Message".format("topic", message_count))
    print "Sending {}".format(message_count)
    message_count += 1
    time.sleep(1)
