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
        #msg = aes.AESCipher(key).encrypt(msg)
        #msg = bf.BlowfishCipher(key).encrypt(msg)
        #msg = sig.Signal().encrypt(msg)
        sig.Signal().test()

        print(msg)

        #encEnt = entropyTest.entropyTest(msg)

        #fields = [plainEnt, encEnt, file]

        #print(fields)
        #writeCSV("BFEntropy"+file[9:11]+".csv", fields)
