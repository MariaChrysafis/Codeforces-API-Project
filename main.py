import rpy2
import json, csv, requests, statistics, bs4
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt
url = "https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false"
response = urlopen(url)
data_json = json.loads(response.read())
results = data_json['result']
df = pd.DataFrame(results)
df.to_csv('users.csv')

c = 0
tot = []
for index, row in df.iterrows() :
    tot.append(row)
tot = pd.DataFrame(tot)
arr = []
for x in tot['maxRating'] :
    arr.append(x)
plt.hist(arr, bins=1000)
plt.show()
print(statistics.mode(arr))
