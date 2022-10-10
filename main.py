import rpy2
import json, csv, requests, statistics, bs4
from urllib.request import urlopen
import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
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
maxrating = []

for x in tot['maxRating'] :
    maxrating.append(x)

rating = []
for x in tot['rating'] :
    rating.append(x)


#rng = np.random.RandomState(0)
#colors = rng.rand(len(maxrating))
#plt.scatter(rating, maxrating, c = colors, alpha=0.1,cmap='viridis')
#plt.show()
#plt.colorbar()
x = rating
y = maxrating

# Calculate the point density
xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=1)
plt.show()
