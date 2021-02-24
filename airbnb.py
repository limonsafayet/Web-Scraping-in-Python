import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&checkin=2021-02-28&checkout=2021-03-05&source=structured_search_input_header&search_type=pagination&ne_lat=21.34812729706493&ne_lng=-157.74456931204463&sw_lat=21.232326394850137&sw_lng=-157.91365576834346&zoom=13&search_by_map=true&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&federated_search_session_id=1559b2e9-ec03-456b-9fa9-a4bb79746f64'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Links':[''], 'Title':[''], 'Details':[''], 'Price':[''], 'Rating':['']})

while True:

    postings = soup.find_all('div', class_='_8s3ctt')
    for post in postings:
        try:
            link = post.find('a', class_='_gjfol0').get('href')
            link_full = 'https://www.airbnb.com' + link
            title = post.find('a', class_='_gjfol0').get('aria-label')
            price = post.find('span', class_='_olc9rf0').text
            rating = post.find('span', class_='_10fy1f8').text
            details = post.find('div', class_='_kqh46o').text

            df = df.append({'Links':link_full, 'Title':title, 'Details':details, 'Price':price, 'Rating':rating}, ignore_index = True)

        except:
            pass

    try:
        next_page = soup.find_all('a', {'aria-label': 'Next'})[0].get('href')
        next_page_url = 'https://www.airbnb.com' + next_page
        page = requests.get(next_page_url)
        soup = BeautifulSoup(page.text, 'lxml')

    except:
        break

df.to_csv('~/Scraped-Data/airbnb_scraped_data.csv')




