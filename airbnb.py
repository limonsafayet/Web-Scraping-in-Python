import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&checkin=2021-02-28&checkout=2021-03-05&source=structured_search_input_header&search_type=pagination&ne_lat=21.34812729706493&ne_lng=-157.74456931204463&sw_lat=21.232326394850137&sw_lng=-157.91365576834346&zoom=13&search_by_map=true&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&federated_search_session_id=1559b2e9-ec03-456b-9fa9-a4bb79746f64'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# Next page url get

next_page = soup.find('a', {'aria-label':'Next'}).get('href')
next_page_url = 'https://www.airbnb.com'+next_page

print(next_page_url)

