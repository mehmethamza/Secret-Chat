# -*- coding:utf-8 -*-
import socket
import decod



mylistener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("ip adresi:")
port = int(input("port:"))
password = input("şifre lütden:")
mylistener.bind((host, port))
mylistener.listen(0) 
c, addr = mylistener.accept()
# Bağlanan istemciye hoşgeldin mesajı gönderilir.
c.sendall(bytes("Merhaba!".encode("utf-8")))

print('{} bağlandı.'.format(addr))

while True:
    
    
    data = str(c.recv(1024))[1:]
    
    
    if data:
        
        data = decod.decoder(password,data)
        data = str(data)
        
        print("Friend: {}".format(data))
        
        respond = input("Me: ")

        respond = decod.encods(password,respond)
        respond = bytes(respond.encode("utf-8"))
        
        
        if respond == "q":
            exit()
        
        else:  
            
            
            c.sendall(respond)