import socket

#target information
sHost = "127.0.0.1" #all local ips 
sPort = 8081

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.connect((sHost, sPort))
print("Connected")

while True:
    sockList = [serv]
#print("Client")z