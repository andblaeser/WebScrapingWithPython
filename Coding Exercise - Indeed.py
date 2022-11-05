#1 input job title into input box

#2 get link, title, company, salary, date, location

#3 do this for every page until no jobs are left

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('D:\chromedriver.exe')

driver.get('https://www.indeed.com/')

login = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
login.send_keys('data analyst')
login.send_keys(Keys.ENTER)

df = pd.DataFrame(columns=['Link', 'Title', 'Company', 'Salary', 'Date', 'Location'])

while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'job_seen_beacon')
  
    for post in postings:
        link = post.find('a', class_ = 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
        full_link = 'https://www.indeed.com'+link
        title = post.find('div', class_ = 'css-1m4cuuf e37uo190').text.strip()
        company = post.find('span', class_ = 'companyName').text.strip()
        try:
            salary = post.find('div', class_ = 'attribute_snippet').text.strip()
        except:
            salary = 'N/A'
        date = post.find('span', class_ = 'date').text.strip()
        try:
            location = post.find('div', class_ = 'companyLocation').text.strip()
        except:
            location = 'N/A'
        df = df.append({'Link':full_link, 'Title':title, 'Company':company, 'Salary':salary, 'Date':date, 'Location':location}, ignore_index=True)
    
    try:
        button = soup.find('a', attrs = {'aria-label': 'Next Page'}).get('href')
        driver.get('https://www.indeed.com'+button)
    except:
        break