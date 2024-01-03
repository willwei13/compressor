import socket
import os
import time


def Get_FilePath_FileName_FileExt(filename):
    filepath, tempfilename = os.path.split(filename)
    shotname, extension = os.path.splitext(tempfilename)
    return filepath, shotname, extension


def udpc():
    global start
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = ('C:\date\ex.zip')
    filepath, shotname, extension = Get_FilePath_FileName_FileExt(filename)
    client_addr = ('127.0.0.1', 9952)
    f = open(filename, 'rb')
    count = 0
    while True:
        if count == 0:
            data = bytes(shotname + extension, encoding="utf8")
            start = time.time()
            s.sendto(data, client_addr)
        data = f.read(1024 * 40)
        if str(data) != "b''":
            s.sendto(data, client_addr)
            # print(str(count) + 'byte')
        else:
            s.sendto('end'.encode('utf-8'), client_addr)
            break
        # data, server_addr = s.recvfrom(1024 * 40)
        count += 1
    print('recircled' + str(count * 40))
    end = time.time()
    # print('cost' + str(round(end - start, 2)) + 's')
    size = os.path.getsize(filename) / 1000
    bili = (count * 40) / size
    f.close()
    s.close()
    return [(end - start),(100 - (bili * 100))]


if __name__ == '__main__':
    a = udpc()
    print(a)
