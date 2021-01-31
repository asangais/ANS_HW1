import socket

HOST = '127.0.0.1'  # loopback
PORT = 6500         # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('b')
    data = s.recv(AMT_DATA)

print('Received', repr(data))


#prints the letter received from server
#terminate the process
