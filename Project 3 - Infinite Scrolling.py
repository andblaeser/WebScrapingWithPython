from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('D:\chromedriver.exe')

driver.get('https://www.nike.com/w/sale-3yaep')

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height =  driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', class_ = 'product-card__body')

df = pd.DataFrame(columns = ['Link', 'Name', 'Subtitle', 'Price', 'Sale Price'])

for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text
        subtitle = product.find('div', class_ = 'product-card__subtitle').text
        full_price = product.find('div', class_ = 'product-price us__styling is--striked-out css-0').text
        sale_price = product.find('div', class_ = 'product-price is--current-price css-1ydfahe').text
        df = df.append({'Link':link, 'Name':name, 'Subtitle':subtitle, 'Price':full_price, 'Sale Price':sale_price}, ignore_index = True)
    except:
        pass

def floatify(series):
    series = series.replace('[\$]', '', regex=True).astype(float)
    return series

df['Discount'] = (floatify(df['Price']) - floatify(df['Sale Price'])) / floatify(df['Price'])
df = df.sort_values(by=['Discount', 'Price'], ascending=False)

df.to_csv('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/nike.csv')