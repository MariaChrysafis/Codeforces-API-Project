import rpy2
import json, csv, requests, statistics, bs4
from urllib.request import urlopen
import pandas as pd
url = "https://codeforces.com/api/problemset.problems?tags=implementation"
response = urlopen(url)
data_json = json.loads(response.read())
results = data_json['result']
problems = results['problems']
df = pd.DataFrame(problems)
df.to_csv('problems.csv')
url = "https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false"
response = urlopen(url)
data_json = json.loads(response.read())
results = data_json['result']
df = pd.DataFrame(results)
df.to_csv('users.csv')

for index, row in df.iterrows() :
    if row['rating'] >= 3000 :
        print(row)
