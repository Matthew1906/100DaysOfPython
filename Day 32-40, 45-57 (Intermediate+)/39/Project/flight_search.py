import requests
from flight_data import FlightData

TEQUILA_URL = "https://tequila-api.kiwi.com/"

TEQUILA_HEADER = {
    'apikey':"yyyESODifzwvd4Bq3pb7L2sv6INUXk7X",
    'accept':'application/json'   
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self): 
        self.data = FlightData()
        pass

    def getIATACode(self, city:str):
        get_params = {
            'term':city,
            'locale':'en-US',
            'location_types':'airport',
            'limit':2,
            'active_only': 'true'
        }
        get_response = requests.get(url = TEQUILA_URL+'locations/query', params=get_params, headers =TEQUILA_HEADER).json()['locations'][0]
        return get_response['id']
    
    def checkLower(self, sheet_data):
        for data in sheet_data:
            check_params = {
                'fly_from':self.data.departure_code,
                'fly_to':data['code'],
                'date_from': self.data.now,
                'date_to':self.data.limit,
                'limit':5,
                'curr':'GBP'
            }
            response = requests.get(url = TEQUILA_URL+'v2/search', params=check_params, headers= TEQUILA_HEADER).json()
            print(response)
            break

            
