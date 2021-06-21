import requests 
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
<<<<<<< HEAD
        self.price_url = 'https://api.sheety.co/67718a1735911fa925ff2fe0c3d43574/flightDealsProject/prices'
        self.user_url = 'https://api.sheety.co/67718a1735911fa925ff2fe0c3d43574/flightDealsProject/users'
        self.header = {'Content-Type':'application/json'}
        self.username = 'dummy'
        self.password = 'dummy1234'
=======

        self.url = 'url'
        self.header = {'Content-Type':'application/json'}
        self.username = 'username'
        self.password = 'password'
>>>>>>> 6fdeb2ae4dacd23aa2c5ffabdc846d50bc73163d

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
<<<<<<< HEAD
        get_result = requests.get(url = self.price_url, auth = (self.username, self.password)).json()['prices']
=======
        get_result = requests.get(url = self.url, auth = (self.username, self.password)).json()['prices']
>>>>>>> 6fdeb2ae4dacd23aa2c5ffabdc846d50bc73163d
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