# DAY 39-40 CAPSTONE PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: FLIGHT CLUB APPLICATION
# THINGS I IMPLEMENTED: API, REQUESTS, API AUTHENTICATION, DATETIME, REGEX, OS

# Import Modules
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from os import system, name
import re

# Define Objects
dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

# Create necessary functions
def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def validateEmail(email):
    email_regex = '^[^@]+@[^@]+[.][^@]+$'
    if(re.search(email_regex, email)):
        return True
    return False

def findFlight():
    '''Function to Find Cheap Flights and Email the customers if found cheap flight'''
    clear()
    # Initialize all data
    user_data = dataManager.getAllUsers()
    price_data = dataManager.getAllPrice()
    if price_data[0]['iataCode'] == '':  
        # Add IATA Codes if it hasn't been defined yet
        cities = dataManager.getAllCities()
        for city in cities:
            dataManager.addIATACode(city, flightSearch.getIATACode(city))
        price_data = dataManager.getAllPrice()
    # Find cheap flights 
    cheap_flights = flightSearch.checkLower(price_data)
    # If there are cheap flights
    if len(cheap_flights)>0:
        for cheap_flight in cheap_flights:
            print(f"Found cheap flight to {cheap_flight.cityTo}!")
            for user in user_data:
                # Send Email
                notificationManager.sendmail(cheap_flight, user['name'], user['email'])
                print(f"Sending email to {user['name']}..")
    input("Press enter to continue..")

def addUser():
    '''Add New User'''
    clear()
    name = input("Please input your name: ")
    email = input("Please input your email: ")
    if not validateEmail(email):
        print("Wrong input! The app will restart...")
        input("Press enter to continue...")
        return
    dataManager.addUser(name, email)
    if not input("Type 'y' to insert another user!: ") == 'y':
        return
    addUser()

# Driver Code
print("Welcome to Matthew's Flight Club")
while True:
    clear()
    choice = input("Type 'find' to look for flights, or type 'add' to insert a new user\n>> ").lower()
    if choice == 'find':
        findFlight()
    elif choice == 'add':
        addUser()
    if not input("Type 'y' to continue!: ") == 'y':
        clear()
        break