import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/reg/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', {'summary':'Standings - Detailed View'})

headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns= headers)

for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_='d3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [tr.text.strip() for tr in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row

print(df)

df.to_csv('~/Scraped-Data/nfl_scraped_data.csv')


