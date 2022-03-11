from Crypto.Cipher import Blowfish

class BlowfishCipher():
    def __init__(self, key):
        self.key = key
        self.blockSize = Blowfish.block_size

    def encrypt(self, msg):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)

        cipherText = cipher.encrypt(msg)
        return cipherText

    def decrypt(self, cipherText):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)

        plainText = cipher.decrypt(cipherText)
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
