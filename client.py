import socket
import select
import sys
import time
import os
from datetime import datetime

import encryption.aes as aes
import encryption.blowfish as bf
from csvFunc import writeCSV

key ="testkey"
maxSize = os.path.getsize("testData/5Mdata.txt")

#target information
sHost = "127.0.0.1" #all local ips
sPort = 8081

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.connect((sHost, sPort))
print("Connected")

print("a: AES\n")
print("b: Blowfish\n")
print("c: Signal")
encMtd = input("Select enc method: ")

def listen():
    #start timer
    decryptStart = time.time()

    recvMsg = serv.recv(maxSize).decode()

    #decrypt
    if encMtd == "a":
        recvMsg = aes.AESCipher(key).decrypt(recvMsg)
    elif encMtd == "b":
        recvMsg = bf.BlowfishCipher(key).decrypt(recvMsg)
    #elif encMtd = "c":
        #signal

    decryptEnd = time.time()

    print(recvMsg)

    decryptTime = decryptEnd - decryptStart

    #writeCSV(encMtd + "decrypt.csv", [decryptTime])

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
            if encMtd == "a":
                msg = aes.AESCipher(key).encrypt(msg)
            elif encMtd == "b":
                msg = bf.BlowfishCipher(key).encrypt(msg)
            #elif encMtd = "c":
                #signal

            #end timer
            encryptEnd = time.time()

            serv.send(msg)#.encode())
            encryptTime = encryptEnd - encryptStart
            sys.stdout.flush()
            #writeCSV("encrypt.csv", encryptTime)

            #writeCSV("size.csv", plainSize)
