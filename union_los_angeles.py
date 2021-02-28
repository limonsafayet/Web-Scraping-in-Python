from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://store.unionlosangeles.com/collections/outerwear')

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_hight = driver.execute_script('return document.body.scrollHeight')
    if(new_hight == last_height):
        break
    last_height = new_hight

soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_='container main')

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''],'Color':[''],'Price':[''],'Sale Price':['']})
for product in product_card:
    try:
        link = product.find('a', class_='product-card__img-link-overlay').get('href')
        name = product.find('div', class_='product-card__title').text
        subtitle = product.find('div', class_='product-card__subtitle').text
        color = product.find('div', class_='product-card__product-count').text
        full_price = product.find('div', class_='product-price css-1h0t5hy').text
        sale_price = product.find('div', class_='product-price is--current-price css-s56yt7').text
        df = df.append({'Link':link, 'Name':name, 'Subtitle':subtitle,'Color':color,'Price':full_price,'Sale Price':sale_price}, ignore_index= True)
    except:
        pass

df.to_csv('~/Scraped-Data/nike_scraped_data.csv')