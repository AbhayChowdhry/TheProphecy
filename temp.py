import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

url = 'https://coinmarketcap.com/tokens/'

driver = webdriver.Chrome()
driver.get(url)

# table = driver.find_elements_by_class_name('sc-f7a61dda-3 kCSmOD cmc-table  ')
table = driver.find_elements(By.XPATH, "//p[@class='sc-e225a64a-0 ePTNty']")

names = set()
number = 0
# height = document.body.scrollHeight/10;
while True:
    for chain in table:
        names.add(chain.text)
    
    driver.execute_script('window.scrollTo(0, {temp}*document.body.scrollHeight/10);'.format(temp=number+1))
    number+=1

    table = driver.find_elements(By.XPATH, "//p[@class='sc-e225a64a-0 ePTNty']")

    if len(names) >= 99: break
    
print(names)
print(len(names))




