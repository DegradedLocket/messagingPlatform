import csv
timeHeaders = ["encrypt", "decrypt"]

sizeHeaders = ["plain", "encrypted"]
def combine():
    encryptFile = open("encryptTime.csv", "r")
    decryptFile = open("decryptTime.csv", "r")

    reader = csv.reader(encryptFile)
    encryptData = list(reader)

    reader = csv.reader(decryptFile)
    decryptData = list(reader)

    combinedData = zip(encryptData, decryptData)

    combinedFile = open("times.csv", "w")
    write = csv.writer(combinedFile)

    write.writerow(timeHeaders)
    write.writerows(combinedData)
