import json
import csv
import requests
from urllib.request import urlopen
import statistics
import bs4
import pandas as pd
url = "https://codeforces.com/api/problemset.problems?tags=implementation"
response = urlopen(url)
data_json = json.loads(response.read())
