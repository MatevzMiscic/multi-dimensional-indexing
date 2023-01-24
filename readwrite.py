import os
import csv
from sort import sort2

def read_csv(filename):
    names = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            names.append((row[0], row[1]))
    return names

def write_csv(filename, rows):
    dir = os.path.dirname(filename)
    if dir:
        os.makedirs(dir, exist_ok=True)
    with open(filename, 'w', encoding='utf-8', newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for row in rows:
            writer.writerow(list(row))



readfile = "in.csv"
writefile = "out.csv"

names = read_csv(readfile)
write_csv(writefile, sort2(names))




