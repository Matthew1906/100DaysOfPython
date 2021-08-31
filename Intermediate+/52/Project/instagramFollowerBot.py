# Day 52 Project of 100 Days of Python
# Project Name: Instagram Follower Bot
# Things i implemented: Selenium, Time

# import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

# Create Constants
CHROME_DRIVER_PATH = YOUR_CHROME_PATH
TARGET_ACCOUNT = input("Insert target account: ")
INSTAGRAM_EMAIL = input("Insert email: ")
INSTAGRAM_PASSWORD = input("Insert password: ")

# Create class
class InstagramBot:
    # Constructor
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    # Login
    def login(self):
        # Go to Instagram login page  
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(3)
        # Input Email
        email_input = self.driver.find_element_by_name('username')
        email_input.send_keys(INSTAGRAM_EMAIL)
        sleep(1)
        # Input Password
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(INSTAGRAM_PASSWORD,Keys.ENTER)
        sleep(1)
    # Find followers
    def find_followers(self):
        sleep(1)
        search_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_input.send_keys(TARGET_ACCOUNT)
        sleep(1)
        search_input.send_keys(Keys.ENTER, Keys.ENTER)
        sleep(3)
        follower_page = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_page.click()
        sleep(2)
        for _ in range(20):
            self.scroll()
            sleep(1)
    # Scroll
    def scroll(self):
        follower_container = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_container)
    # Follow
    def follow(self):
        followers = self.driver.find_elements_by_css_selector('li button')
        for follower in followers:
            sleep(1)
            try:
                follower.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_css_selector('button.aOOlW.HoLwm')
                cancel_button.click()
            finally:
                sleep(1)

instagram_bot = InstagramBot()
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()