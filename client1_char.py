import socket

HOST = '127.0.0.1'  # loopback
PORT = 6500         # The port used by the server
char = "k"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #sends a character to server process
    s.send(char)
    
#wait for server process closure and terminate process
    
