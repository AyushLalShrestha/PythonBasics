
import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    while True:
        s.listen(1)
        conn, addr = s.accept()
        print("Connection from: " + str(addr))
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print("from connected user: " + data)
            data = data.upper()
            print("sending: " + data)
            conn.send(data.encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    main()

