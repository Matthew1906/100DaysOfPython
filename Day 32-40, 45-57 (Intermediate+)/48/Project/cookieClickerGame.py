# Day 48 Project of 100 Days of Python
# Project Name: Cookie Clicker Game Automation
# Things i implemented: Selenium webdriver, datetime

# Import modules
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import datetime as dt

# get the driver path
chrome_driver_path = 'C:/Users/matth/OneDrive/Documents/ProgrammingLanguagesLearning/Python/Development/chromedriver'

# Create the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Go to the website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Sometimes the program crashes, i dunno why
cookie = driver.find_element_by_id("bigCookie")
old_time = dt.datetime.now()

while True:
    new_time = dt.datetime.now()
    time_diff = new_time-old_time
    time_diff = round(time_diff.total_seconds(),0)
    if time_diff%5==0:
        products = driver.find_elements_by_css_selector('.unlocked.enabled')
        if len(products)>0:
            try:
                products[-1].click()
            except ElementClickInterceptedException:
                pass
    else:
        cookie.click()