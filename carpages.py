import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Links': [''], 'Title': [''], 'Price': [''], 'Color': ['']})

for i in range(20):

    postings = soup.find_all('div', class_='media soft push-none rule')
    for post in postings:
        try:
            link = post.find('h4', class_='hN')
            link_full = 'https://www.carpages.ca' + link.find('a').get('href')
            title = link.find('a').get('title')
            price = post.find('strong', class_='delta').text.strip()
            color_div = post.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1]
            color = color_div.find('span').text.strip()
            df = df.append({'Links': link_full, 'Title': title, 'Price': price, 'Color': color}, ignore_index=True)

        except:
            pass
    next_page_url = soup.find('a', class_='nextprev').get('href')
    page = requests.get(next_page_url)
    soup = BeautifulSoup(page.text, 'lxml')


df.to_csv('~/Scraped-Data/carpages_scraped_data.csv')




