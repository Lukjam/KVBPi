from bs4 import BeautifulSoup
import os
import pandas as pd
import requests
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
url = "https://www.kvb.koeln/generated/?aktion=show&code=733&title=text&bgcolor=ffffff&color=000000"
response = requests.get(url, headers=hdr)
soup = BeautifulSoup(response.content,'lxml')
table = soup.find_all('table')[1]
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))
line = df[0].values.tolist()
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
with open(dir_path+'/Data/example.csv', 'w') as examplefile:
    wr = csv.writer(examplefile, quoting=csv.QUOTE_ALL)
    wr.writerow(line)
print(line)