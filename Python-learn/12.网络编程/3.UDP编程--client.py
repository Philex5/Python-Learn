import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(('127.0.0.1', 9999))

for data in [b'Philex', b'Jack', b'Jeremy']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()