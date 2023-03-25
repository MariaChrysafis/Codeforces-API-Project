import json, csv, requests, statistics, bs4
from urllib.request import urlopen
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
import urllib.request
from scipy.stats import lognorm
from urllib.parse import quote
import urllib
import requests
from slugify import slugify
import pandas as pd
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
df = get_data(url, 'people.csv')[1]
rating = []
maxRating = []
for index, rows in df.iterrows() :
    url = "https://codeforces.com/api/user.status?handle="
    try :
        url += rows['handle']
        s = rows['handle'] + ".csv"
        df1 = get_data(url, s)
        a = rows['rating']
        b = rows['contribution']
        print(url)
        for index1, row1 in df1.iterrows() :
            try :
                print("GOT")
            except :
                print("NOPE")
    except :
        continue
    rating.append(a)
    maxRating.append(b)
print(rating)
print(maxRating)
plt.plot(rating, maxRating, 'ro')
plt.show()
