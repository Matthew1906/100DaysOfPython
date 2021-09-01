import requests,datetime as dt
from flight_data import FlightData
from os import getenv
from dotenv import load_dotenv

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self): 
        '''Flight Search Contructor'''
        self.url = "https://tequila-api.kiwi.com/"
        self.header = {
            'apikey':getenv('FLIGHT_KEY'),
            'accept':'application/json'   
        }

    def getIATACode(self, city:str):
        '''Get IATA Code'''
        get_params = {
            'term':city,
            'locale':'en-US',
            'location_types':'airport',
            'limit':2,
            'active_only': 'true'
        }
        get_response = requests.get(url = self.url+'locations/query', params=get_params, headers = self.header).json()['locations'][0]
        return get_response['id']
    
    def checkLower(self, sheet_data):
        '''Find Cheap Flights'''
        results = []
        for data in sheet_data:
            check_params = {
                'fly_from':'CGK',
                'fly_to':data['iataCode'],
                'date_from': dt.datetime.now().strftime('%d/%m/%Y'),
                'date_to':(dt.datetime.now() + dt.timedelta(days = 30)).strftime('%d/%m/%Y'),
                'limit':1,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                'curr':'GBP'
            }
            try:
                response = requests.get(url = self.url+'v2/search', params=check_params, headers= self.header).json()['data'][0]
            except IndexError:
                pass
            else:
                if response['price']<=data['lowestPrice']:
                    new_flight_data = FlightData(
                        response['flyFrom'],
                        response['flyTo'],
                        response['cityTo'],
                        response['countryTo']['name'],
                        response['price'],
                        response['local_departure'],
                        response['local_arrival'],
                        response['deep_link']
                    )
                    results.append(new_flight_data)
        return results