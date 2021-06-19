import requests 

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = 'url'
        self.header = {'Content-Type':'application/json'}
        self.username = 'username'
        self.password = 'password'

    def getIndex(self, city:str):
        get_result = requests.get(url = self.url, auth = (self.username, self.password)).json()['prices']
        res = 0
        for idx in range(len(get_result)):
            if get_result[idx]['city']==city:
                res = idx
                break
        return str(res+2)

    def getAll(self):
        get_result = requests.get(url = self.url, auth = (self.username, self.password)).json()['prices']
        return [{'code':data['iataCode'], 'price':data['lowestPrice']} for data in get_result]

    def getAllCities(self):
        get_result = requests.get(url = self.url, auth = (self.username, self.password)).json()['prices']
        return [data['city'] for data in get_result]

    def addIATACode(self, city:str, code:str):
        change_params = {
            'price':{
                'city':city,
                'iataCode':code
            }
        }
        change_index = self.getIndex(city)
        requests.put(url = self.url+f'/{change_index}', headers = self.header, auth = (self.username,self.password), json = change_params)
    
