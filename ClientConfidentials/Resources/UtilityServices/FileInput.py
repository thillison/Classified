# Import API Dataset

import csv

def load_csv(csvpath):
    with open(csvpath, "r") as csv_file:
        data = []
        csvreader = csv.reader(csv_file, delimiter = ",")
        for row in csvreader:
            data.append(row)

    return data