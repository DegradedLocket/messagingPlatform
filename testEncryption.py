import sys
#import time
#from datetime import datetime

import encryption.aes as aes
import encryption.blowfish as bf
import encryption.signal2 as sig
import entropyTest

from csvFunc import writeCSV

fields = []

key = "testKey"

#files = ["testData/1Kdata.txt", "testData/5Kdata.txt",
#         "testData/1Mdata.txt", "testData/5Mdata.txt"]

files = ["testData/engLipsum.txt"]
#importFile = sys.argv[1]
#numOfTests = int(sys.argv[1])
numOfTests = 1

for file in files:
    testDataFile = open(file, "r")
    testData = testDataFile.read()
    for _ in range(numOfTests):
        msg = testData

        #start timer

        #plainSize = sys.getsizeof(msg)
        #plainEnt = entropyTest.entropyTest(msg)

        #encrypt
        #encmsg = aes.AESCipher(key).encrypt(msg)
        #writeCSV("AESEncrypt"+file[9:11]+".csv", fields)
        #writeCSV("AESDecrypt"+file[9:11]+".csv", fields)
        #encmsg = bf.BlowfishCipher(key).encrypt(msg)
        #writeCSV("BFEncrypt"+file[9:11]+".csv", fields)
        #writeCSV("BFDecrypt"+file[9:11]+".csv", fields)
        #msg = sig.Signal().encrypt(msg)
        sig.test()

        #print(msg)

        #encEnt = entropyTest.entropyTest(msg)

        #fields = [plainEnt, encEnt, file]

        #print(fields)
        #writeCSV("BFEntropy"+file[9:11]+".csv", fields)
