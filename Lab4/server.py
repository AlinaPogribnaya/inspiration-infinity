import socket
import time

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socks.bind(("localhost", 13))
socks.listen(5)
conn, addr = socks.accept()

print ("TCPServer Waiting for client on port 13")

while True:
    data = conn.recv(1024).decode()
    if (data != 'Q' and data != 'q'):
        have_connect = 1  # if all clients are disconnected
    while have_connect:
        print(data)
        if (data != 'Q' and data != 'q'):
            data = ('On server now: ' + time.asctime(time.localtime()) + '\n')
            conn.send(data.encode())
        else:
            conn.close()
