# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint

# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open('largequakes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    sniff = csv.Sniffer()
    sample = csvfile.read(1024)
    csvfile.seek(0)
    if sniff.has_header(sample):
        next(reader)
    for row in reader:
        result.append({"Place": row[0], "Mag": row[1], "Link": row[2], "Time": row[3]})

pprint.pp(result)
