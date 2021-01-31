import socket

HOST = "127.0.0.1" #loopback
PORT1 = 6500 #non-priveleged <1023
PORT2 = 6501 #non-priveleged <1023

#create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#bind the socket
    s.bind ((HOST,PORT1))
    s.bind ((HOST,PORT2))
#listening socket
    s.listen()
#blocking mode accept ()
    conn, addr = s.accept()
    with conn:
        while True:
#server receives original character from Client 1
            x = conn.recv(1)
#server will decrement original character received by client1 
            i = ord(char[0])
            i -= 1
            y = chr(i)
#closure of Client1 socket
     s.close()
            
#server will send new character to client 2
            s.sendall(y)
            
#wait for closure from client 2 and terminate process

