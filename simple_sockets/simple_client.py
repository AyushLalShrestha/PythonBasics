import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    while True:
        message = raw_input("Enter message: ")
        print message
        while message != 'q':
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            # print('Server responds : ' + data)
            # message = raw_input("-> ")
    s.close()


if __name__  == '__main__':
    main()



