from selenium import webdriver

chrome_driver_path = YOUR_OWN_CHROME_DRIVER_PATH
# give the selenium the right driver, so that it can interact well with the browser

# Create the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # Using Selenium for the Amazon Price Bot -> did not work i dunno why
# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
# prices = driver.find_elements_by_css_selector("#size_name_0_price > p")[0]

# print(prices.text)

