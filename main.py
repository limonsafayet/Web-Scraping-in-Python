import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

print(soup)
