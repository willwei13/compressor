import socket, os, time

server = socket.socket()
server.bind(('127.0.0.1', 6649))
server.listen()

print("等待....")
while True:
    conn, addr = server.accept()
    print("new conn:", conn)
    while True:
        data = conn.recv(1024*40)
        if not data:
            print("client is disconnection")
            break
        cmd, filename = data.decode().split()
        print(filename)

        if os.path.isfile(filename):
            f = open(filename, 'rb')
            '''
            file_size = os.stat(filename).st_size
            conn.send((str(file_size)).encode())
            conn.recv(1024*40)
            '''
            for line in f:
                conn.send(line)
            f.close()
