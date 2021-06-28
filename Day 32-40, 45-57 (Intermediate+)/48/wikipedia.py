# Import Module
from selenium import webdriver #Get webdriver
from selenium.webdriver.common.keys import Keys # insert keys

# Driver path
chrome_driver_path = 'C:/Users/matth/OneDrive/Documents/ProgrammingLanguagesLearning/Python/Development/chromedriver'

# Create the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Go to the website
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# We can click a link
article_count = driver.find_element_by_xpath("//*[@id='articlecount']/a[@title='Special:Statistics']")
# article_count.click()

# We can also input something
search_input = driver.find_element_by_id("searchInput")
search_input.send_keys("Python", Keys.ENTER)

# Quit the driver
driver.quit()