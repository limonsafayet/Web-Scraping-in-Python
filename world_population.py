import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

print (soup)
