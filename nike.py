from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('nike')
box.send_keys(Keys.ENTER)

time.sleep(10)
imdb_website = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/a/h3').click()

time.sleep(10)
imdb_website = driver.find_element_by_xpath('/html/body/div[1]/div[3]/header/div/div[1]/div[2]/nav/div[2]/ul/li[6]/a').click()

time.sleep(10)
imdb_website = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/button/i').click()

last_height = driver.execute_script('return document.body.scrollHeight')
print(last_height)
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_hight = driver.execute_script('return document.body.scrollHeight')
    if(new_hight == last_height):
        break
    last_height = new_hight

soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_='product-card__body')

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