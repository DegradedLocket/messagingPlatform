from Crypto.Cipher import Blowfish
import hashlib
import base64

class BlowfishCipher():
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.blockSize = Blowfish.block_size


    def encrypt(self, msg):
        msg = self.padding(msg)
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)

        cipherText = base64.b64encode(cipher.encrypt(msg.encode()))
        return cipherText

    def decrypt(self, cipherText):
        cipherText = base64.b64decode(cipherText)

        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)

        plainText = cipher.decrypt(cipherText)
        return self.unPad(plainText).decode("utf-8")


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
