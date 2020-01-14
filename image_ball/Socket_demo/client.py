import socket
import time
s = socket.socket()
host = socket.gethostname()
port = 8086
s.connect((host,port))
while True:
    print(s.recv(1024).decode())
    time.sleep(0.01


               )