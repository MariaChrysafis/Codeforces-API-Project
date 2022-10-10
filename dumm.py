import json
import csv
# import pandas as pd
import pandas as pd
# df = pd.read_json (r'/Users/maria/PycharmProjects/active1retired0.json')
# df.to_csv (r'/Users/maria/PycharmProjects/active1retired0.csv', index = None, sep='|', columns=['status', 'result'])
filename = r'/Users/maria/PycharmProjects/active1retired0.csv'
with open(filename, newline = '') as f :
    reader = csv.reader(f)
    for row in reader :
        print(row)
