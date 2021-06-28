from selenium import webdriver

chrome_driver_path = 'C:/Users/matth/OneDrive/Documents/ProgrammingLanguagesLearning/Python/Development/chromedriver'
# give the selenium the right driver, so that it can interact well with the browser

# Create the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Go to the website
driver.get("https://www.python.org/")

# Get all tags
tags = driver.find_elements_by_css_selector("#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")

# Put them into a dictionary
events = {}
for i in range(len(tags)):
    event = tags[i].text.split("\n")
    events[str(i+1)] = {
        'time':event[0],
        'name':event[1]
    }

# Print the dictionary
print(events)

# Quit the driver
driver.quit()