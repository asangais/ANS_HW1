import socket

HOST = "127.0.0.1" #loopback
PORT = 6500 #non-priveleged <1023

#create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#bind the socket
    s.bind ((HOST,PORT))
#listening socket
    s.listen()
#blocking mode accept ()
    conn, addr = s.accept()
    with conn:
        while True:
#server receives original integer from Client 1
            x = conn.recv(1)
#server will decrement original integer received by client1 
            x += 1
            if not x:
                break
            print(x)


#server will decrement alphabetic character received by client1
#clientsocket.send(bytes("Hey there!!!","utf-8"))
#server will send new character to client 2
#wait for closure from client 2 and terminate process


#ori_char = "t"
#i = ord(char[0])
#i += 1
#new_char = chr(i)
#print(f"New letter is {new_char}")
