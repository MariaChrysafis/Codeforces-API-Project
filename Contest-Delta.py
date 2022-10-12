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
    try :
        response = urlopen(url)
    except :
        return [False, pd.DataFrame()]
    data_json = json.loads(response.read())
    results = data_json['result']
    df = pd.DataFrame(results)
    df.to_csv(file)
    return [True, df]

df_codeforces_round_list = get_data("https://codeforces.com/api/contest.list?gym=false", 'rounds.csv')[1]
tot = []
c = 0
for index, rows in df_codeforces_round_list.iterrows() :
    if rows['relativeTimeSeconds'] < 0 :
        continue
    url = "https://codeforces.com/api/contest.ratingChanges?contestId="
    url += str(rows['id'])
    print(url)
    x = get_data(url, 'rating_change.csv')
    if not x[0] :
        continue
    df_codeforces_round_rating_change = x[1]
    for index1, rows1 in df_codeforces_round_rating_change.iterrows() :
        tot.append(rows1['newRating'] - rows1['oldRating'])
plt.hist(tot, range = [min(tot) - 1, max(tot) + 1], bins = 1000)
plt.show()
plt.hist(tot, range = [min(tot) - 1, max(tot) + 1], bins = 1000, log = True)
plt.show()
# print(tot)
print("MEAN", statistics.mean(tot))
print("STDEV", statistics.stdev(tot))
print("MEDIAN", statistics.median(tot))
print("VARIANCE", statistics.variance(tot))
print("MODE", statistics.multimode(tot))
# statistics.NormalDist
