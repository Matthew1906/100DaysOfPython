# Import Module
from selenium import webdriver #Get webdriver
from selenium.webdriver.common.keys import Keys # insert keys

# Driver path
chrome_driver_path = 'C:/Users/matth/OneDrive/Documents/ProgrammingLanguagesLearning/Python/Development/chromedriver'

# Create the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Go to the page
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Dummy")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Account")

email = driver.find_element_by_name("email")
email.send_keys("dummyaccount@gmail.com")

submit = driver.find_element_by_xpath("/html/body/form/button")
submit.click()

# driver.quit()