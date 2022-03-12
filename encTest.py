import blowfish, aes

#key = [0x4B7A70E9, 0xB5B32944, 0xDB75092E, 0xC4192623,
#       0xAD6EA6B0, 0x49A7DF7D, 0x9CEE60B8, 0x8FEDB266,
#       0xECAA8C71, 0x699A17FF, 0x5664526C, 0xC2B19EE1,
#       0x193602A5, 0x75094C29]
key = "topsercretkey"

msg = "testingtestingtesting"#input("Enter Message: ")

cipherText = blowfish.BlowfishCipher(key).encrypt(msg)
#cipherText = aes.AESCipher(key).encrypt(msg)
print(cipherText)

#plainText = aes.AESCipher(key).decrypt(cipherText)
plainText = blowfish.BlowfishCipher(key).decrypt(cipherText)
print(plainText)
