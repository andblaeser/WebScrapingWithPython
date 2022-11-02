import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', {'summary': 'Standings - Detailed View'})

headers = []

for i in table.find_all('th'):
    headers.append(i.text.strip())

df = pd.DataFrame(columns = headers)

for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [td.text.strip() for td in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row

df.to_csv('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/nfl_stats.csv')