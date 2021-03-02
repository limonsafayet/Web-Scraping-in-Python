from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://www.indeed.com/')

input_job_name = driver.find_element_by_xpath('//*[@id="text-input-what"]')
input_job_name.send_keys('data analyst')

input_location = driver.find_element_by_xpath('//*[@id="text-input-where"]')
input_location.send_keys('New York, NY')
time.sleep(5)
find_job = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/div/div/div/form/div[3]').click()

# Creates a dataframe
df = pd.DataFrame({'Link': [''], 'Job Title': [''], 'Company': [''], 'Location': [''], 'Salary': [''], 'Date': ['']})

# This loop goes through every page and grabs all the details of each posting
# Loop will only end when there are no more pages to go through
while True:
    # Imports the HTML of the current page into python
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Grabs the HTML of each posting
    postings = soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')

    # grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        link = post.find('a', class_='jobtitle turnstileLink').get('href')
        link_full = 'https://www.indeed.com/' + link
        name = post.find('h2', class_='title').text.strip()
        company = post.find('span', class_='company').text.strip()
        try:
            location = post.find('div', class_='location accessible-contrast-color-location').text.strip()
        except:
            location = 'N/A'
        date = post.find('span', class_='date').text.strip()
        try:
            salary = post.find('span', class_='salaryText').text.strip()
        except:
            salary = 'N/A'
        df = df.append(
            {'Link': link_full, 'Job Title': name, 'Company': company, 'Location': location, 'Salary': salary,
             'Date': date},
            ignore_index=True)

    # checks if there is a button to go to the next page, and if not will stop the loop
    try:
        button = soup.find('a', attrs={'aria-label': 'Next'}).get('href')
        driver.get('https://www.indeed.com/' + button)
    except:
        break

df['Date_num'] = df['Date'].apply(lambda x: x[:2].strip())

def integer(x):
    try:
        return int(x)
    except:
        return x

df['Date_new'] = df['Date_num'].apply(integer)
df.sort_values(by= ['Date_new', 'Salary'], inplace= True)

df = df[['Link', 'Job Title', 'Company', 'Location', 'Salary', 'Date']]
df.to_csv('~/Scraped-Data/indeed_scraped_data.csv')


#####################################################################################

#Code below sends an email to whomever through python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'account@gmail.com'
receiver = 'account@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('A/File/Path/indeed_jobs.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="indeed_jobs.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'account@gmail.com', password = 'input your password')
s.sendmail(sender, receiver, msg.as_string())
s.quit()
