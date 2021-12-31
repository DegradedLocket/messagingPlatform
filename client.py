import socket
from datetime import datetime

#target information
sHost = "127.0.0.1" #all local ips 
sPort = 8081

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.connect((sHost, sPort))
print("Connected")

while True:
    sockList = [serv]
    
    msg = input("Type: ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    msg = str(date + " : " + msg)
    
    serv.send(msg.encode())
#print("Client")zHe