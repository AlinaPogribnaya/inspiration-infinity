import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 13))
data=input()
sock.send(data.encode())

answer= sock.recv(1024).decode()
sock.close()
print('Результат работы сервера: ', answer)
