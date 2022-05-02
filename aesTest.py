from ctypes import sizeof
import encryption.aes as aes

msg="Hello"
key="testkey"

encmsg = aes.AESCipher(key).encrypt(msg)
print(encmsg)

enc3 = "b'QmYxgyd2b3ACSHNJcx/EM+9W5v9uK0xea1RFdE9a2Pg='"
b = enc3[1:]
by = bytes(b, "utf-8")

print(by)

decmsg1 = aes.AESCipher(key).decrypt(by)
#print(enc2)

print(decmsg1)
