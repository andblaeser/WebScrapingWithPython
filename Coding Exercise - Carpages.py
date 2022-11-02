import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame(columns = ['Link', 'Name', 'Price', 'Color'])

postings = soup.find_all('div', class_ = 'media soft push-none rule')

pageCount = 1

while (pageCount <= 15):
    postings = soup.find_all('div', class_ = 'media soft push-none rule')
    for post in postings:
        link = post.find('a', class_ = 'media__img media__img--thumb').get('href')
        link_full = 'https://www.carpages.ca'+link
        name = post.find('h4', class_ = 'hN').text.strip()
        price = post.find('strong', class_ = 'delta').text.strip()
        color = post.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'Link': link_full, 'Name': name, 'Price': price, 'Color': color}, ignore_index=True)

    next_page = soup.find('a', {'title': 'Next Page'}).get('href')
    next_page_full = 'https://www.carpages.ca'+next_page
    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    pageCount += 1
    
df.to_csv('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/carpages.csv')