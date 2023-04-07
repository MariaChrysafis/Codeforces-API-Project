import pandas as pd
import os
import glob
import json
import csv
path = "/Users/maria/PycharmProjects/pythonProject5/data/problems.csv" # change path accordingly
print(path)
dictionary = dict()
ans = 0
with open(path, 'r' ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        ans += 1
        c = '1'
        for i in range(0, 11) :
            s = 'tags/'
            s += str(i)
            x = line[s]
            if x == "" :
                continue
            print(line)
            dictionary[x] = dictionary.get(x, 0) + 1
    print(ans)
print(dictionary)
