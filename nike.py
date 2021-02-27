from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

time.sleep(5)
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