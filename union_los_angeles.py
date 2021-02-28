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

section = soup.find('div', {'id':'main', 'role':'main'})
products = section.find_all('li')
df = pd.DataFrame({'Link':[''], 'Vendor':[''], 'Title':[''],'Price':['']})
for product in products:
    try:
        link = product.find('a').get('href')
        vendor = product.find('p', class_='cap-vendor').text
        title = product.find('p', class_='cap-title').text
        price = product.find('p', class_='cap-price').text

        df = df.append({'Link':link, 'Vendor':vendor, 'Title':title,'Price':price}, ignore_index= True)
    except:
        pass

df.to_csv('~/Scraped-Data/union-los-angeles_scraped_data.csv')