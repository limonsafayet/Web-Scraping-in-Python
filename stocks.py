import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# Price of the stock
price = soup.find('bg-quote', class_ = 'value').text

print("Price : "+ price)

# Closing price of the stock

close_price = soup.find('td', class_ = 'table__cell u-semi').text

print("Closing Price : "+ close_price)

# 52 week range (Lower, Upper)

nested = soup.find('mw-rangebar', class_ ='element element--range range--yearly')

lower = nested.find_all('span', class_ = 'primary')[0].text

print ("52 week range Lower Price : "+lower)

upper = nested.find_all('span', class_ = 'primary')[1].text

print ("52 week range Upper Price : "+upper)

# Analyst Rating

avg = soup.find('li', class_ = 'analyst__option active').text

print("Analyst Ratings :  "+ avg)