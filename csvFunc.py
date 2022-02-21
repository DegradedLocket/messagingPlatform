import csv


def writeCSV(fileName, val):
    f = open(fileName, "a")

    csvWriter = csv.writer(f)

    csvWriter.writerow(val)