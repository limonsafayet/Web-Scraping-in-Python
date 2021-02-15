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

tag.string

# Attributes
tag = soup.header.a
tag.attrs0


#####################################

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

# find
soup.find('header')

soup.header.attrs

soup.find('div', {'class':'container test-site'})

soup.find('h4', {'class':'pull-right price'})


# find_all - part 1
soup.find_all('h4', {'class':'pull-right price'})[6:]

soup.find_all('a', class_ = 'title')

soup.find_all('p', class_ = 'pull-right')


# find_all - part 2
soup.find_all(['h4','p','a'])

soup.find_all(id = True)

soup.find_all(string = 'Iphone')

import re

soup.find_all(string = re.compile('Nok'))

soup.find_all(string = ['Iphone', 'Nokia 123'])

soup.find_all(class_ = re.compile('pull'))

soup.find_all('p', class_ = re.compile('pull'))

soup.find_all('p', class_ = re.compile('pull'), limit = 3)


# find_all - part 3
product_name = soup.find_all('a', class_ = 'title')
product_name

price = soup.find_all('h4', class_ = 'pull-right price')
price

reviews = soup.find_all('p', class_ = re.compile('pull'))
reviews

description = soup.find_all('p', class_ = 'description')
description


product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)

price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)


reviews_list = []
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)


descriptions_list = []
for i in description:
    descriptions2 = i.text
    descriptions_list.append(descriptions2)

import pandas as pd

table = pd.DataFrame({'Product Name':product_name_list, 'Description':descriptions_list,
                     'Price':price_list, 'Reviews':reviews_list})

# print(table)

# extracted data from nested HTML tags
boxes = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')[6]
boxes

boxes.find('a').text

boxes.find('p', class_='description').text

box2 = soup.find_all('ul', class_='nav', id='side-menu')[0]

box2.find_all('li')[1].text






