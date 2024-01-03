import socket, time, os


def ftpc():
    client = socket.socket()
    client.connect(("127.0.0.1", 6649))
    file = 'C:\date\ex.zip'
    while True:
        cmd = 'get ' + file
        time1 = time.time()
        if len(cmd) == 0: continue
        if cmd.startswith("get"):
            client.send(cmd.encode())
            '''
            server_response = client.recv(1024 * 40)
            print("server response: ", server_response)
            client.send(b"ready to recv file")
            file_total_size = int(server_response.decode())
            '''
            file_total_size = os.path.getsize(file)
            received_size = 0
            filename = cmd.split()[1]
            f = open(filename + ".new", "wb")
            while received_size < file_total_size:
                data = client.recv(1024 * 40)
                received_size += len(data)
                f.write(data)
            time2 = time.time()
            '''
            print("total：", file_total_size, " present: ", received_size)
            print(str(time2 - time1))
            size1 = os.path.getsize(file)
            size2 = os.path.getsize(filename + ".new")
            print(str(size2 / size1))
            '''
            break
        else:
            print("file has received done!")
    f.close()
    client.close()
    return [(time2 - time1), (100 - ((received_size / file_total_size) * 100))]


if __name__ == '__main__':
    a = ftpc()
    a1 = a[0]
    a2 = a[1]
    print(a1)
    print(a2)
