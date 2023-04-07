import pandas as pd
import os
import statistics
import glob
import matplotlib.pyplot as plt
import json
import csv

# use glob to get all the csv files
# in the folder
path = "/Users/maria/PycharmProjects/pythonProject5/data/people.csv"
print(path)
dictionary = dict()
ans = 0
tot = []
with open(path, 'r') as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        ans += 1
        # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
        # e.g. print( line[ 'workers' ] ) yields 'w0'
        x = line['rating']
        tot.append(int(x))
    print(ans)
print(tot)
print("MEAN", statistics.mean(tot))
print("STDEV", statistics.stdev(tot))
print("MEDIAN", statistics.median(tot))
print("VARIANCE", statistics.variance(tot))
print("MODE", statistics.multimode(tot))
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Rating Distribution")
plt.hist(tot, range = [min(tot) - 1, max(tot) + 1], bins = 1000)
plt.show()
