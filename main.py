import requests
from bs4 import BeautifulSoup

# Getting the HTML from a website
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

soup

# Tags

soup.head
soup.div

# Navigable Strings
tag = soup.header.p

print(tag.string)
