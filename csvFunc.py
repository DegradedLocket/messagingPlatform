import csv


def writeCSV(fileName, fields):
    f = open(fileName, "a")

    csvWriter = csv.writer(f)

    csvWriter.writerow(fields)