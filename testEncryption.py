import sys
import time
import base64
#from datetime import datetime

import encryption.aes as aes
import encryption.blowfish as bf
import encryption.signal2 as sig
import entropyTest

from csvFunc import writeCSV

encFields = []
decFields = []
sizeFields = []
entFields = []

key = "testKey"

files = ["testData/1Kdata.txt", "testData/5Kdata.txt",
         "testData/1Mdata.txt", "testData/5Mdata.txt"]

#files = ["testData/engLipsum.txt"]
#importFile = sys.argv[1]
numOfTests = int(sys.argv[1])
#numOfTests = 1

key = sig.KeyPair.generate()

r1 = sig.Signal(key=key)
r2 = sig.Signal(pubKey=key.pub)

assert not r1.canSend()
assert r2.canSend()

for file in files:
    testDataFile = open(file, "r")
    testData = testDataFile.read()
    for _ in range(numOfTests):
        msg = testData

        plainSize = sys.getsizeof(msg)
        plainEnt = entropyTest.entropyTest(msg)

        #encrypt
        encryptStart = time.time()
        #encmsg = aes.AESCipher(key).encrypt(msg)
        #writeCSV("AESEncrypt"+file[9:11]+".csv", fields)

        #encmsg = bf.BlowfishCipher(key).encrypt(msg)
        #writeCSV("BFEncrypt"+file[9:11]+".csv", fields)
        encMsg = sig.Signal().encrypt(msg, r1, r2)

        encryptEnd = time.time()

        encryptTime = encryptEnd - encryptStart
        encFields = [encryptTime, file]

        encSize = sys.getsizeof(encMsg["ciphertext"]) + sys.getsizeof(encMsg["header"])
        sizeFields = [plainSize, encSize]


        #decrypt
        decryptStart = time.time()
        #writeCSV("AESDecrypt"+file[9:11]+".csv", fields)
        #writeCSV("BFDecrypt"+file[9:11]+".csv", fields)
        sig.Signal().decrypt(encMsg, r1, r2)
        decryptEnd = time.time()

        decryptTime = decryptEnd - decryptStart
        decFields = [decryptTime, file]

        #writeCSV("SigEncrypt"+file[9:11]+".csv", encFields)
        #writeCSV("SigDecrypt"+file[9:11]+".csv", decFields)
        writeCSV("SigSize"+file[9:11]+".csv", sizeFields)

        #encEnt = entropyTest.entropyTest(encMsg["ciphertext"])

        #entFields = [plainEnt, encEnt, file]

        #writeCSV("SigEntropy.csv", entFields)
