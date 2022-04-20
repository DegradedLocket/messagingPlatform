import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher():
    def __init__(self, key):
        self.blockSize = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, msg):
        #encrypt
        msg = self.padding(msg)

        #setting init vector
        iv = Random.new().read(self.blockSize)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        cipherText = base64.b64encode(iv + cipher.encrypt(msg.encode()))

        return cipherText

    def decrypt(self, cipherText):
        #decrypt
        cipherText = base64.b64decode(cipherText)

        iv = cipherText[:self.blockSize]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        plainText = cipher.decrypt(cipherText[self.blockSize:])
        plainText = self.unPad(plainText).decode("utf-8")

        return plainText

    def padding(self, msg):
        sizeOfPad = self.blockSize - (len(msg) % self.blockSize)
        padding = chr(sizeOfPad)

        padding = padding * sizeOfPad

        paddedText = msg + padding

        return paddedText

    def unPad(self, msg):
        #get the last character of message and use that to set how much padding to remove
        lastChar = msg[len(msg) - 1:]
        sizeOfPad = ord(lastChar)

        unPadText = msg[:-sizeOfPad]

        return unPadText
