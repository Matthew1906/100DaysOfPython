# Import modules
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from utils import *
from time import sleep
from math import ceil
from pandas import DataFrame
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Constants
CHROME_DRIVER_PATH = getenv('CHROME_PATH')
UDEMY_URL = 'https://www.udemy.com/courses/development/'
UDEMY_PARAMS = {
    'lang':'en',
    'ratings':4.5,
    'sort':'highest-rated',
    'persist_locale':'',
    'locale':'en_US'
}
UDEMY_CATEGORIES = [
    'Web Development','Data Science',
    'Mobile Apps','Programming Languages',
    'Game Development', 'Databases',
    'Software Testing', 'Software Engineering',
    'Development Tools', 'No Code Development'
]

# Utility functions
def get_url(index:int):
    '''Create an endpoint based on input'''
    endpoint = '-'.join([value.lower() for value in UDEMY_CATEGORIES[index].split(' ')])
    params = '&'.join([f'{param}={value}' for param, value in UDEMY_PARAMS.items()])
    return UDEMY_URL + endpoint + '/?' + params

# Choose Category
choice = UDEMY_CATEGORIES.index('Web Development')

# Setup Driver
driver = Chrome(executable_path=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(get_url(choice))

# Get Number of Pages
sleep(5)
num_result = driver.find_element_by_class_name('filter-panel--item-count--2JGx3')
num_result = num_result.text.replace(',','')
page_num = ceil(int(num_result[:-8].strip())/16)
all_courses = []

# Scrape the Website
for i in range(page_num):
    sleep(15)
    courses = driver.find_elements_by_css_selector('.course-list--container--3zXPS .browse-course-card--link--3KIkQ')
    for course in courses:
        values = course.text.split('\n')
        print(values)
        result = {
            'name':values[0],
            'description':get_description(values),
            'instructor':get_instructor(values),
            'rating':get_rating(values),
            'reviews':get_reviews(values),
            'total_hours': get_total_hours(values),
            'num_of_lectures': get_num_of_lectures(values),
            'difficulty': get_difficulty(values),
            'price': get_price(values),
            'badge': get_badge(values)
        }
        all_courses.append(result)
    try:
        next_page = driver.find_element_by_class_name('pagination--next--164ol')
        next_page.click() 
    except NoSuchElementException:
        break
driver.quit()

# Put into csv file
df = DataFrame(all_courses)
filename = '-'.join([value.lower() for value in UDEMY_CATEGORIES[choice].split(' ')])
df.to_csv(f'./results/{filename}.csv', index=False)
