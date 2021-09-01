# Import modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
from os import getenv

driver_path = getenv('CHROME_PATH')
job_link = 'https://www.linkedin.com/jobs/search/?geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom'
email = getenv('EMAIL')
password = getenv('PASSWORD')

# Set up Driver
driver = webdriver.Chrome(executable_path = driver_path)

# Go to link
driver.get(job_link)

# Go to Sign in Page
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

# Insert necessary keys
username = driver.find_element_by_id("username")
username.send_keys(email)

user_pass = driver.find_element_by_id("password")
user_pass.send_keys(password)

submit_btn = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
submit_btn.click()

# Get all Job recommendations
available_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable") 

for available_job in available_jobs:
    try:
        available_job.click()
        sleep(1)
        save_button = driver.find_element_by_css_selector(".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary")
        save_button.click()
        sleep(2)
    except NoSuchElementException:
        pass
driver.quit()
