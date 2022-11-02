import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com/s/Honolulu--HI/homes?adults=2&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&refinement_paths%5B%5D=%2Fhomes&checkin=2022-11-04&checkout=2022-11-06&tab_id=home_tab&query=Honolulu%2C%20HI&flexible_trip_lengths%5B%5D=one_week&price_filter_num_nights=2&ne_lat=21.34830556957963&ne_lng=-157.72847706998556&sw_lat=21.2198635753372&sw_lng=-157.88623387540548&zoom=13&search_by_map=true&search_type=user_map_move'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame(columns = ['Links', 'Title', 'Details', 'Price', 'Rating'])
scraping = True

while (scraping == True):
    postings = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
    
    for post in postings:
        try:
            link = post.find('a', class_ = 'ln2bl2p dir dir-ltr').get('href')
            link_full = 'https://www.airbnb.com'+link
            title = post.find('div', class_ = 't1jojoys dir dir-ltr').text
            price = post.find('span', class_ = '_tyxjp1').text
            rating = post.find('span', class_ = 'r1dxllyb dir dir-ltr').text
            details = post.find('span', class_ = 't6mzqp7 dir dir-ltr').text
            df = df.append({'Links': link_full, 'Title': title, 'Details': details, 'Price': price, 'Rating': rating}, ignore_index=True)
        except:
            pass

    try:
        next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
        next_page_full = 'https://www.airbnb.com'+next_page
        url = next_page_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
    except:
        scraping = False
    
df.to_csv('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/multiple_pages.csv')