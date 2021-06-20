#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

dataManager = DataManager()
flightData = FlightData()
flightSearch = FlightSearch()

cities = dataManager.getAllCities()

for city in cities:
    dataManager.addIATACode(city, flightSearch.getIATACode(city))

data  = dataManager.getAll()

flightSearch.checkLower(data)

