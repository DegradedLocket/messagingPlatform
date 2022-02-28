
from Crypto import Random
from Crypto.Cipher import AES

numRounds = 14
blockSize = 16
blocks = []


def padding(msg):
    sizeOfPad = blockSize - (len(msg) % blockSize)
    padding = chr(sizeOfPad)

    padding = padding * sizeOfPad

    paddedText = msg + padding

def unPad(msg):
    #get the last character of message and use that to set how much padding to remove
    lastChar = msg[len(msg) - 1:]
    sizeOfPad = ord(lastChar)

    unPadText = msg[:-sizeOfPad]


def subBytes():
    for i in range(4):
        for j in range(4):
            #substitute

def shiftRows():
    #shiftRows

def mixColumns():
    #mixCols

def addRoundKeys():
    #addRoundKeys

def encrypt():
    #encrypt
    msg = padding(msg)

def decrypt():
    #decrypt
