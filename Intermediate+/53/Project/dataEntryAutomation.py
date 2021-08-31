# Day 53 Capstone Project of 100 Days of Python
# Project Name: Data Entry Job Automation
# Things i implemented: Requests, Beautiful Soup, Selenium, Time

# 1. Import Modules
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 2. Setup Constants
CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
FORMS_URL = 'https://forms.gle/8Tgv5EhWzv4HGpWTA'
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-118.27334129615998%2C%22east%22%3A-71.69131004615998%2C%22south%22%3A20.11041089232061%2C%22north%22%3A52.69600585535755%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D'
ZILLOW_HEADER = {
    'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# 3. Make Soup
zillow_page = requests.get(url=ZILLOW_URL, headers=ZILLOW_HEADER).text
zillow_soup = BeautifulSoup(zillow_page, 'html.parser')

# 4. Parse the Soup
zillow_links = zillow_soup.find_all(name='a', class_='list-card-link')
zillow_addresses = zillow_soup.find_all(class_='list-card-addr')
zillow_details = zillow_soup.find_all(class_='list-card-price')

# 5. Open Chrome
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# 6. Fill out forms 
for i in range(len(zillow_addresses)):
    driver.get(FORMS_URL)
    sleep(1)
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(zillow_addresses[i].get_text())
    sleep(1)
    detail_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    detail_input.send_keys(zillow_details[i].get_text())
    sleep(1)
    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(zillow_links[i*2]['href'])
    sleep(1)
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_btn.click()
# 7. Close Driver
driver.quit()
    
