import socket
from threading import Thread
import os

#server settings
sHost = "0.0.0.0" #all local ips
sPort = 8081

cliSocks = [] #list of clients

maxSize = os.path.getsize("testData/5Mdata.txt")

serv = socket.socket()

serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind((sHost, sPort)) #bind socket to address and port

#start listening for connections
serv.listen(2)
print("Server @ " + sHost + ":" + str(sPort))

def listen(cs):
    #code to listen for client
    while True:
        msg = cs.recv(maxSize).decode()
        if msg:
            peername = cs.getpeername()
            print(str(peername[1]) + " - " + msg)

            #send msg
            for cli in cliSocks:
                cli.send(msg.encode())
        else:
            cliSocks.remove(cs)


#print("Server")

while True:
    cliSock, cliAddr = serv.accept()
    cliSocks.append(cliSock)

    t = Thread(target=listen, args=(cliSock,))

    t.daemon = True

    t.start()
    print("Client " + str(cliAddr) +  " connected")
