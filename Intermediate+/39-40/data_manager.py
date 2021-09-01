import requests 
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price_url = getenv('PRICE_URL')
        self.user_url = getenv('USER_URL')
        self.header = {'Content-Type':'application/json'}
        self.username = getenv('DATA_USERNAME')
        self.password = getenv('DATA_PASS')

    def getIndex(self, city:str):
        get_result = requests.get(url = self.price_url, auth = (self.username, self.password)).json()['prices']
        res = 0
        for idx in range(len(get_result)):
            if get_result[idx]['city']==city:
                res = idx
                break
        return str(res+2)

    def getAllPrice(self):
        get_result = requests.get(url = self.price_url, auth = (self.username, self.password)).json()['prices']
        return get_result

    def getAllCities(self):
        get_result = requests.get(url = self.price_url, auth = (self.username, self.password)).json()['prices']
        return [data['city'] for data in get_result]

    def addIATACode(self, city:str, code:str):
        change_params = {
            'price':{
                'city':city,
                'iataCode':code
            }
        }
        change_index = self.getIndex(city)
        requests.put(url = self.price_url+f'/{change_index}', headers = self.header, auth = (self.username,self.password), json = change_params)
    
    def getAllUsers(self):
        get_result = requests.get(url = self.user_url, auth = (self.username, self.password)).json()['users']
        return get_result

    def addUser(self, name, email):
        user_params = {
            'user':{
                'name':name,
                'email':email
            }
        }
        requests.post(url = self.user_url, headers = self.header, auth = (self.username, self.password), json = user_params)
        print("Insertion successful")