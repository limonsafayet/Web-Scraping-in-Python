# Part 1

from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('https://www.goat.com/sneakers')

# Find using xpath

price = driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/p/span').text

# Find using xpath and loop

for i in range(30):
    price = driver.find_element_by_xpath('//*[@id="'+str(i)+'"]/div[2]/div/p/span').text

    print(price)

# ----------------------------------------------------------------------------------------------
# Part 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

# sending Text into an Input Box

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')

box.send_keys('web scraping')
box.send_keys(Keys.ENTER) # Press Enter

# Clicking on a button

button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
button.click()   # Press Search Button

# Taking a screenshot

driver.save_screenshot('~/Scraped-Data/screenshot.png') # Saving the screenshot

# Self-Scrolling
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[4]/div/div[1]/div/div[1]/div/div[3]/a').click()

driver.execute_script('return document.body.scrollHeight')

driver.execute_script('window.scrollTo(0, 6000)')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# Wait times

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[4]/div/div[1]/div/div[1]/div/div[3]/a')))




