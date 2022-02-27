import socket
import select
import sys
import time
from datetime import datetime

from csvFunc import writeCSV

#target information
sHost = "127.0.0.1" #all local ips
sPort = 8081

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.connect((sHost, sPort))
print("Connected")

def listen():
    #start timer
    decryptStart = time.time()

    msg = serv.recv(2048).decode()

    #decrypt
    decryptEnd = time.time()

    print("\n" + msg)

    decryptTime = decryptEnd - decryptStart

    #writeCSV("decrypt.csv", decryptTime)

while True:
    sockList = [sys.stdin,serv]
    readSock, writeSock, errSock = select.select(sockList,[],[])
    for sock in readSock:
        if sock == serv:
            listen()
        else:
            msg = sys.stdin.readline()

            #start timer
            encryptStart = time.time()

            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            msg = str(date + " : " + msg)

            plainSize = sys.getsizeof(msg)
            #encrypt

            #end timer
            encryptEnd = time.time()

            serv.send(msg.encode())

            encryptTime = encryptEnd - encryptStart

            #writeCSV("encrypt.csv", encryptTime)

            #writeCSV("size.csv", plainSize)
