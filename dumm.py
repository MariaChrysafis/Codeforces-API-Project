import rpy2
import json, csv, requests, statistics, bs4
from urllib.request import urlopen
import pandas as pd
url = "https://codeforces.com/api/problemset.problems?tags=implementation"
response = urlopen(url)
data_json = json.loads(response.read())
results = data_json['result']
problems = results['problems']
print(problems)
print(type(problems))
df = pd.DataFrame(problems)
df.to_csv('problems.csv')