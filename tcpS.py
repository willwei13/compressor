import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,0)
s.bind(('127.0.0.1', 9884))
s.listen(5)
print('Waiting for connection...')
count = 0
received_size = 0
while True:
    sock, addr = s.accept()
    print('Accept new connection from %s:%s...' % addr)

    if count == 0:
        data1 = sock.recv(1024 * 40)
        print(str(data1))
    file_total_size = int(data1.decode())
    received_size = 0
    sock.send('received'.encode())
    data = sock.recv(1024 * 40)
    filepath = str(data.decode())

    f = open(filepath, 'wb')
    while received_size < file_total_size:
        data = sock.recv(1024 * 40)
        f.write(data)
        received_size += len(data)
    data = sock.recv(1024 * 40)
    if data == b'end':
        s.close()
        f.close()
        break
print('已接收 ', received_size, ' Byte')