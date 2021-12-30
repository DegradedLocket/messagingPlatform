import socket

#server settings
sHost = "0.0.0.0" #all local ips 
sPort = 8081
sepToken = "<SEP>"

cliSocks = [] #list of clients

serv = socket.socket()

serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind((sHost, sPort)) #bind socket to address and port

#start listening for connections
serv.listen(2)
print("Server @ " + sHost + ":" + str(sPort))

def listen(cs):
    #code to listen for client
    msg = cs.recv(2048)
    
    if msg:
        msg = msg.replace(sepToken, ":")
        
        #send msg
    else:
        cliSocks.remove(cs)
    
#print("Server")

while True:
    cliSock, cliAddr = serv.accept()
    cliSocks.append(cliSock)
    
    print("Client " + str(cliAddr) +  " connected")
