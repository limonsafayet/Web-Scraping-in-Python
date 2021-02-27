# Part 1
"""
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('https://www.goat.com/sneakers')

# xpath

price = driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/p/span').text

# xpath and loop

for i in range(30):
    price = driver.find_element_by_xpath('//*[@id="'+str(i)+'"]/div[2]/div/p/span').text

    print(price)
"""

# Part 2
# sending Text into an Input Box

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')

box.send_keys('web scraping')
box.send_keys(Keys.ENTER)

# Clicking on a button
