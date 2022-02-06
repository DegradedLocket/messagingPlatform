import csv, os.path

fileName = "results.csv"

fields = ["cSend", "ServRecv", "ServSend", "cRecv"]
rows = []

def writeCSV(field, val):
    if os.path.isfile(fileName):
        new = True

    f = open(fileName, "a")

    csvWriter = csv.writer(f)

    if new:
        csvWriter.writerow(fields)

    csvWriter.writerow(val)
