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
print(df)


