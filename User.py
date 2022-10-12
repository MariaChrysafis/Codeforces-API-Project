import math, sys, requests, json, csv
import pandas as pd
from urllib.request import urlopen
def get_data (url, file):
    response = urlopen(url)
    data_json = json.loads(response.read())
    results = data_json['result']
    df = pd.DataFrame(results)
    df.to_csv(file)
    return [True, df]
print("Type in your handle")
val = input()
print("Greetings, " + val + "! Please stand by. It may take some time")
url = "https://codeforces.com/api/user.status?handle="
url += val
print(url)
df = get_data(url, 'test.csv')[1]
rating = []
mySet = set()
for index, rows in df.iterrows() :
    try :
        a = rows['problem']['contestId']
        b = rows['problem']['rating']
    except :
        continue
    if rows['verdict'] != 'OK' :
        continue
    mySet.add(str(rows['problem']['contestId']) + str(rows['problem']['index']))
    # print(rows['problem']['index'])
for i in mySet :
    print(i)
print(len(mySet))
