import requests, datetime as dt
from data_manager import DataManager

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.departure_code = 'CGK'
        self.now = dt.datetime.now().strftime('%d/%m/%Y')
        self.limit = (dt.datetime.now() + dt.timedelta(days = 30)).strftime('%d/%m/%Y')


