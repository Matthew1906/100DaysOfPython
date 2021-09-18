# /-------------------------------------- START PROGRAM --------------------------------------/

# Import modules
from selenium.webdriver import Chrome  
from selenium.webdriver.common.keys import Keys 
from pyautogui import locateOnScreen, click, press, moveTo
from dotenv import load_dotenv
from time import sleep
from os import getenv

# /-------------------------------------- PREPARATIONS --------------------------------------/

# Load Environment variables
load_dotenv()

# Constants
LOGIN_URL = 'https://www.kaggle.com/account/login'
SEARCH_URL = 'https://www.kaggle.com/datasets'
CHROME_DRIVER_PATH = getenv('CHROME_PATH')
EMAIL = getenv('KAGGLE_EMAIL') 
PASSWORD = getenv('KAGGLE_PASSWORD')

# Utility Functions
get_url = lambda keyword: f'{SEARCH_URL}?search={keyword.lower()}&fileType=csv&sizeStart=10%2CMB&sizeEnd=50%2CMB&datasetsOnly=true'

# Get keyword
keyword = '+'.join(input('What topic of dataset would you like to search?> ').strip().split())

# Setup Driver
driver = Chrome(executable_path=CHROME_DRIVER_PATH)

# /-------------------------------------- LOGIN TO KAGGLE --------------------------------------/

# Go to url
driver.get(LOGIN_URL)

# Click login with email (google is way too secure)
sleep(5)
login_with_email = driver.find_element_by_xpath('//*[@id="site-container"]/div[1]/div/form/div[2]/div/div[2]/a/li/div')
login_with_email.click()

# Insert Credentials
sleep(5)
insert_credentials = driver.find_elements_by_class_name('mdc-text-field__input')
insert_credentials[0].click()
insert_credentials[0].send_keys(EMAIL)
insert_credentials[1].click()
insert_credentials[1].send_keys(PASSWORD, Keys.ENTER)

# /-------------------------------------- DOWNLOAD DATASET --------------------------------------/

# Go to url
sleep(5)
driver.get(get_url(keyword))
sleep(5)

# Click the ellipsis and download button
moveTo(locateOnScreen('./images/ellipsis.png'))
click()
sleep(1)
moveTo(locateOnScreen('./images/download_dataset.png'))
click()

# Wait for download
sleep(30)
driver.quit()

# /-------------------------------------- UNZIP DOWNLOADED DATASET --------------------------------------/

# Locate and click
for image_to_locate in ['desktopSearch.png', 'downloads.png', 'enlarge.png']:
    moveTo(locateOnScreen(f'./images/{image_to_locate}'))
    click()
    sleep(5)

# Extract All
sleep(2)
moveTo(locateOnScreen('./images/dataset.png'))
click(button='right')
sleep(2)
moveTo(locateOnScreen('./images/extract.png'))
click()
sleep(2)
press('enter')

# /-------------------------------------- END --------------------------------------/