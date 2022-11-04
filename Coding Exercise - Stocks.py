import requests
from bs4 import BeautifulSoup

#1. remember to import the HTML into python
url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#2. price of the stock
price = soup.find('bg-quote', class_ = "value").text

#3. closing price of the stock
close = soup.find('td', class_ = 'table__cell u-semi').text

#4. 52 week range (lower, upper)
rangebar = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')

yearlyRange = rangebar.find_all('span', class_ = 'primary')

low, high = yearlyRange[0].text, yearlyRange[1].text

#5. analyst rating
rating = soup.find('li', class_ = 'analyst__option active').text

price, close, low, high, rating