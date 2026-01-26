import socket

SERVER_IP = '10.1.66.163'  # IP of the server machine
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    s.sendall(b'Hello, server!')
    data = s.recv(1024)

print('Received:', data.decode())