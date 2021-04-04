
import time
import zmq
import pprint


def result_collector():
    context = zmq.Context()
    receiver_socket = context.socket(zmq.PULL)
    receiver_socket.bind("tcp://127.0.0.1:5558")

    while True:
        result = receiver_socket.recv_json()
        print("result received: {}".format(result))
        time.sleep(4)


result_collector()
