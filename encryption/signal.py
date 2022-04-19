from base64 import encode
import random
from axolotl.util.keyhelper import KeyHelper
from axolotl.sessioncipher import SessionCipher
from axolotl.sessionbuilder import SessionBuilder
from axolotl.tests.inmemoryaxolotlstore import InMemoryAxolotlStore
from axolotl.protocol.whispermessage import WhisperMessage


class Signal():
    def __init__(self):
        self.devID = 1
        self.recvID = 2

        self.store = InMemoryAxolotlStore()

        self.sBuilder = SessionBuilder(self.store, self.store, self.store, self.store, self.recvID, self.devID)

        self.sCipher = SessionCipher(self.store, self.store, self.store, self.store, self.recvID, self.devID)

    def encrypt(self, msg):
        encodedMsg = msg.encode()


        cipherText = self.sCipher.encrypt(encodedMsg)

        return cipherText

    def decrypt(self, msg):
        msg = self.sCipher.decryptMsg(msg)

        return msg
