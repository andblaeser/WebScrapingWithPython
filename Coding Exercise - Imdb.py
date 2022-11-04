#1 set google as your starting page and type in top 100 movies of all time in the box
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\chromedriver.exe')

driver.get('https://www.google.com/')

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('top 100 movies of all time')

#2 press enter and then click on the link corresponding to imdb
box.send_keys(Keys.ENTER)

link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3')
link.click()

#3 create a wait time for the entire page to load
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img')))

#4 scroll all the way down to where the movie jaws appears
driver.execute_script('window.scrollTo(0, 23000)')

#5 take screen shot of the actual page, and get the image of the jaws poster
driver.save_screenshot('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/jaws_page.png')
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot('D:/Udemy/Web Scraping in Python with BeautifulSoup and Selenium/Coding Exercises/jaws_poster.png')