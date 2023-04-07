import pandas as pd
import os
import glob
import json
import csv
# use glob to get all the csv files
# in the folder
path = "/Users/maria/PycharmProjects/pythonProject5/data/users/"
print(path)
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
dictionary = dict()
c = 0
for f in csv_files:
    # print("YES")
    # read the csv file
    c += 1
    df = pd.read_csv(f)
    for index, rows in df.iterrows() :
        try :
            s = rows['problem'].split()
            for i in range(len(s)) : 
                if s[i] == "'rating':" :
                    dictionary[s[i + 1]] = dictionary.get(s[i + 1], 0) + 1
        except :
            assert False
    if c % 100 == 0 :
        print(c)
        print(dictionary)
for (key, value) in dictionary.items() :
    print(key, value)

