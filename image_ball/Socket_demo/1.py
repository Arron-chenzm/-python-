import socket

s = socket.socket()
host = socket.gethostname()
port = 8086
s.bind((host,port))
s.listen(5)
i = 1
c,address = s.accept()
while True:

    print("get connet from",address)
    i = i+1
    c.send("{}".format(i).encode())
    c.send("{}".format(i).encode())

