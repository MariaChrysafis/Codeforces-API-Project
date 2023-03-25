import math, sys, requests, json, csv
import pandas as pd
from urllib.request import urlopen
def get_data (url, file):
    print("OKAY")
    response = urlopen(url)
    print("YES")
    data_json = json.loads(response.read())
    print("YES")
    results = data_json['result']
    df = pd.DataFrame(results)
    df.to_csv(file)
    return [True, df]
print("Get list of rated users")
url = "https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false"
print(url)
df = get_data(url, 'people.csv')
