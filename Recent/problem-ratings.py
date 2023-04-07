import pandas as pd
import os
import glob
import json
import csv
# use glob to get all the csv files
# in the folder
path = "/Users/maria/PycharmProjects/pythonProject5/data/problems.csv"
print(path)
dictionary = dict()
ans = 0
with open(path, 'r' ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        ans += 1
        # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
        # e.g. print( line[ 'workers' ] ) yields 'w0'
        x = line['rating']
        dictionary[x] = dictionary.get(x, 0) + 1
    print(ans)
print(dictionary)
