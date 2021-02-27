from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time imdb')
box.send_keys(Keys.ENTER)
time.sleep(10)
imdb_website = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/a/h3').click()
time.sleep(10)

driver.execute_script('window.scrollTo(0, 12000)')

driver.save_screenshot('~/Scraped-Data/imdb_screenshot.png')

driver.close()
