# ------------------------------------------------ producer.py ------------------------------------------------
import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    for num in xrange(20000):
        work_message = {'num': num}
        zmq_socket.send_json(work_message)

producer()


# ------------------------------------------------ middleware consumer.py ------------------------------------------------
import time
import zmq
import random

def consumer():
    consumer_id = random.randrange(1, 10005)
    print "I am consumer #%s" % (consumer_id)
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = {'consumer': consumer_id, 'num': data}
        if data % 2 == 0:
            consumer_sender.send_json(result)

consumer()


# ------------------------------------------------ result_collector.py ------------------------------------------------
import time
import zmq
import pprint

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    for x in xrange(1000):
        result = results_receiver.recv_json()
        if collecter_data.has_key(result['consumer']):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1
        if x == 999:
            pprint.print(collecter_data)

result_collector()


"""
run the commands:
    python resultcollector.py
    python consumer.py
    python consumer.py
    python producer.py


Expected Output:
    {
    3362: 233,
    9312: 767
    }

"""
