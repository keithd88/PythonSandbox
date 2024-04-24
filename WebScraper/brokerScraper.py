from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import pandas as pd

# search settings
zip_code = 32043
radius = "100" # can be 0, 5, 10, 25, 50, or 100

browser = webdriver.Chrome()
browser.get('https://forms.nabip.org/consumer/findagent2.cfm')

# enter zip code
browser.find_element(By.NAME, 'zip').send_keys(zip_code)

# enter radius
radius_select = Select(browser.find_element(By.NAME, 'miles'))
radius_select.select_by_visible_text('Single Zip Code') 
radius_select.select_by_value(radius)

# search database
browser.find_element(By.NAME, 'zip').send_keys(Keys.ENTER)



html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

# find total num of brokers in area
total_brokers = soup.find_all('p')

# check there are results
if len(total_brokers) == 1:
    print("No members found")
    exit()

total_brokers = int(total_brokers[1].text.split()[4])


brokers = {}
   
# extract broker info
new_brokers = soup.find('div', {'class': 'contentContainer'})

new_brokers = new_brokers.find_all('div')

for num, broker in enumerate(new_brokers):
    data_dict = {}
    data_dict['name'] = broker.find('div').text
    
    print(broker)

