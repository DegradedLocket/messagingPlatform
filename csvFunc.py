import csv


def writeCSV(fileName, fields):
    f = open("results/" + fileName, "a+")

    csvWriter = csv.writer(f)

    csvWriter.writerow(fields)