import base64

from nacl.bindings.crypto_scalarmult import crypto_scalarmult

import doubleratchet
#from doubleratchet.ratchets import SymmetricKeyRatchet

from nacl.public import PrivateKey as Curve25519DecryptionKey
from nacl.public import PublicKey as Curve25519EncryptionKey


class SendReceiveChain(doubleratchet.kdfchains.ConstKDFChain):
    def __init__(self, key):
        super(SendReceiveChain, self).__init__(
            "const_data".encode(),
            doubleratchet.recommended.RootKeyKDF("SHA-512", "RootKeyKDF info string".encode()),
            key
        )


class SymmetricKeyRatchet(doubleratchet.ratchets.SymmetricKeyRatchet):
    def __init__(self):
        super(SymmetricKeyRatchet, self).__init__(SendReceiveChain, SendReceiveChain)


class RootChain(doubleratchet.kdfchains.KDFChain):
    def __init__(self):
        super(RootChain, self).__init__(
            doubleratchet.recommended.RootKeyKDF(
                "SHA-512",
                "IAmARootChain".encode()
            ),
            "I am a root key!".encode()
        )

class KeyPair(doubleratchet.KeyPair):
    def __init__(self, priv = None, pub = None):
        wrap = self.__class__.__wrap

        self.__priv = wrap(priv, Curve25519DecryptionKey)
        self.__pub = wrap(pub,  Curve25519EncryptionKey)

        if not self.__priv == None and self.__pub == None:
            self.__pub = self.__priv.public_key

    @classmethod
    def generate(cls):
        return cls(priv = Curve25519DecryptionKey.generate())

    @staticmethod
    def __wrap(key, cls):
        if key == None:
            return key

        if isinstance(key, cls):
            return key

        return cls(key)

    def serialize(self):
        pub = self.pub
        pub = None if pub == None else base64.b64encode(
            bytes(pub)).decode("US-ASCII")

        priv = self.priv
        priv = None if priv == None else base64.b64encode(
            bytes(priv)).decode("US-ASCII")

        return {
            "super": super(KeyPair, self).serialize(),
            "pub": pub,
            "priv": priv
        }

    @classmethod
    def fromSerialized(cls, serialized, *args, **kwargs):
        self = super(KeyPair, cls).fromSerialized(
            serialized["super"],
            *args,
            **kwargs
        )

        if serialized["pub"] != None:
            self.__pub = cls.__wrap(
                base64.b64decode(serialized["pub"].encode("US-ASCII")),
                Curve25519EncryptionKey
            )

        if serialized["priv"] != None:
            self.__priv = cls.__wrap(
                base64.b64decode(serialized["priv"].encode("US-ASCII")),
                Curve25519DecryptionKey
            )

        return self

    @property
    def pub(self):
        return None if self.__pub == None else bytes(self.__pub)

    @property
    def priv(self):
        return None if self.__priv == None else bytes(self.__priv)

    def getSharedSecret(self, other):
        if self.__priv == None:
            raise MissingKeyException(
                "Cannot get a shared secret using this KeyPair, private key missing."
            )

        if other.__pub == None:
            raise MissingKeyException(
                "Cannot get a shared secret using the other KeyPair, public key missing."
            )

        return crypto_scalarmult(
            self.priv,
            other.pub
        )


class Signal(doubleratchet.ratchets.DoubleRatchet):
    def __init__(self, key=None, pubKey=None):
        super(Signal, self).__init__(
            doubleratchet.recommended.CBCHMACAEAD(
                "SHA-512", "ExampleCBCHMACAEADConfig".encode()), 5, SymmetricKeyRatchet(), "some associated data".encode(),
            KeyPair,
            RootChain(),
            key,
            pubKey
        )
    def _makeAD(self, header, ad):
            return ad

    def encrypt(self, msg, r1, r2):
        cipherText = r2.encryptMessage(msg.encode())
        return cipherText

    def decrypt(self, msg, r1, r2):
        plainText = r1.decryptMessage(msg["ciphertext"], msg["header"])
        return plainText.decode()

