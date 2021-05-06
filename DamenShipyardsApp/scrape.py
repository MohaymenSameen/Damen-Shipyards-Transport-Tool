from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from csv import writer
from selenium.webdriver.common.keys import Keys
import time

url = "https://eschenker.dbschenker.com/app/tracking-public/?refNumber=27690040156446"

driver = webdriver.Firefox(executable_path='/Users/mohaymen/Documents/GitHub/Damen-Shipyards-Transport-Tool/node_modules/geckodriver/geckodriver')

driver.get(url)

time.sleep(5) #This is the fix

driver_cookies = driver.get_cookies()
c = {c['name']:c['value'] for c in driver_cookies}
res = requests.get(driver.current_url,cookies=c)
soup = BeautifulSoup(res.text,"lxml")

print(soup)


