# -*- coding:utf-8 -*-
import socket
import decod

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("ip adresi:")
port = int(input("port:"))
password = input("şifre lütden:")

# Sunucuya bağlanalım.
s.connect((host, port))

# İstemci sunucuya bağlandıktan sonra 
# Sunucunun yaptığı işin aynısını yapıyor.
while True:
    data = str(s.recv(1024))[1:]
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
            s.sendall(respond)