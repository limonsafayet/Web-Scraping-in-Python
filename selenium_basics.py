from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('https://www.goat.com/sneakers')

# xpath

price = driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/p/span').text

# xpath and loop

for i in range(30):
    price = driver.find_element_by_xpath('//*[@id="'+str(i)+'"]/div[2]/div/p/span').text

    print(price)





