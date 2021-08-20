# Web Scraping in Python
Web Scraping in Python with Beautifulsoup and Selenium. 

## Description

In this project, data are scrap from websites using python with Beautifulsoup and Selenium. 

## Web Scraping using Beautifulsoup

### In basics.py

Here are the basics of Beautifulsoup. How to use Beautifulsoup functions to get data from websites.

### In stocks.py

Here from (https://www.marketwatch.com/investing/stock/aapl) this website, 5 types of data are scraped. They are price of stock, closing price, 52 week range lower, 52 week range upper, analyst rating. 

### In world_population.py

Here from (https://www.worldometers.info/world-population/) this website World Population data is scraped and stored into Scraped-Data folder in CSV format. 

### In nfl.py

Here from (https://www.nfl.com/standings/league/2019/reg/) this website National Football League data is scraped and stored into Scraped-Data folder in CSV format. 

### In airbnb.py

Here ***Multiple Web Page*** data have been scraped from https://www.airbnb.com and those data are stored into Scraped-Data folder in CSV format. 

### In carpages.py

Here 1 to 20 number pages data have been scraped from https://www.carpages.ca and those data are stored into Scraped-Data folder in CSV format. 

## Web Scraping using Selenium

### In selenium_basics.py

Here are the basics of Selenium. How to scrape data using **XPATH**, Sending Text into an **Input Box**, Clicking on a **Button**, Taking a **Screenshot**, **Self-Scrolling**, Wait Times.

### In imdb.py

Here first set google as starting page and type ***"top 100 movies of all time imdb"*** in the search box. Then press Enter and click on the link corresponding to IMDb. After that create a wait time for the entire page to load. Scroll down to where the 50th movie appears. Then take a screenshot of the page. 

### In nike.py

Here first set google as starting page and type ***"nike"*** in the search box. Then press Enter and click on the link corresponding to Nike. After that create a wait time for the entire page to load. Then click on **Sell** and close the popup. Then started **Infinite Scrolling**. When it reached the bottom of that page then scraped data using ***Beautifulsoup*** and stored those data into Scraped-Data folder in CSV format.

### In union_los_angeles.py

Here from (https://store.unionlosangeles.com/collections/outerwear) this website data are scraped. First using selenium go to that website,  wait time for the entire page to load. Then started **Infinite Scrolling**. When it reached the bottom of that page then scraped data using ***Beautifulsoup*** and stored those data into Scraped-Data folder in CSV format.

### In twitter.py

Here celebrity tweets are scraped. First using selenium user name and password entered into input filed and login button pressed. Then in the search box of the home page celebrity name is entered automatically. Then using Beautifulsoup tweets and scraped and store them in a list. 

### In indeed.py

Here from (https://www.indeed.com) job post data are scraped. First, enter the job name and location into the input box and click the search button using selenium. Then grabs the HTML of each posting and scraped those data. Then sort those data by Date also stores those data into Scraped-Data folder in CSV format. Then Email automatically to those email addresses. 
