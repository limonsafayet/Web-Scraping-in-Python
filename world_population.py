import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')

headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns= headers)

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row

print(df)

df.to_csv('~/Scraped-Data/world_population_scraped_data.csv')


