import time
import zmq

def result_collector(receiver_socket):
   # print(receiver_socket.getsockopt(zmq.RCVBUF))
   result = receiver_socket.recv_json()
   print("received: {}".format(result))
   return result


def message_sender(sender_socket, result):
   sender_socket.send_json(result)


def main():
   context = zmq.Context()
   receiver_socket = context.socket(zmq.PULL)
   receiver_socket.connect("tcp://127.0.0.1:5557")
   
   publisher_socket = context.socket(zmq.PUSH)
   publisher_socket.connect("tcp://127.0.0.1:5558")
   
   while True:
      json_message = result_collector(receiver_socket)
      if json_message.get('action') == 'login':
         json_message['vulnerabilty'] = 'HIGH'
      else:
         json_message['vulnerabilty'] = 'LOW'
      
      message_sender(publisher_socket, json_message)
      time.sleep(1)

if __name__=="__main__":
   main()

   
   


