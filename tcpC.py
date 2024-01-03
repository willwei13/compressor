import socket
import os
import time


def tcpc():
    filename = 'C:\date\ex.zip'
    start = time.time()
    filesize = str(os.path.getsize(filename))
    fname1, fname2 = os.path.split(filename)
    f = open(filename, 'rb')
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
    s.connect(('127.0.0.1', 9884))
    while True:
        if count == 0:
            s.send(filesize.encode())
        s.recv(1024 * 40)
        s.send(fname2.encode())
        for line in f:
            s.send(line)
        s.send(b'end')
        count = count + 1
        break
    end = time.time()
    return end-start


if __name__ == '__main__':
    a = tcpc()
    print(a)
