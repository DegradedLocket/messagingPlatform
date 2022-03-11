import socket
import sys
import time
from datetime import datetime

from csvFunc import writeCSV

fields = []

importFile = sys.argv[1]
numOfTests = int(sys.argv[2])

testDataFile = open(importFile, "r")
testData = testDataFile.read()

#target information
sHost = "127.0.0.1"  # all local ips
sPort = 8081

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.connect((sHost, sPort))
print("Connected")

for _ in range(numOfTests):
    msg = testData

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
    sys.stdout.flush()

    fields = [encryptTime, importFile]

    writeCSV("encrypt.csv", fields)

    #writeCSV("size.csv", plainSize)
