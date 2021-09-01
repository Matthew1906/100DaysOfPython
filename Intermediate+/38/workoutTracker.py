# Requires input of personal data and private api
import requests, datetime as dt

APP_ID = 'appid'
API_KEY = 'apikey'

workout_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

workout_headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

workout_name = input("Tell me what exercises you did: ")

workout_params = {
    'query': workout_name,
    'gender':'male',
    'age':19,
    'weight_kg':74,
    'height_cm':169,
}

response = requests.post(url=workout_url, headers = workout_headers, json=workout_params).json()

sheety_url = 'url'

sheety_headers = {
    'Content-Type':'application/json'
}

sheety_username = 'username'
sheety_password = 'password'

now = dt.datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime('%X')

for exercise in response['exercises']:
    sheety_params = {
        'workoutTracker':{
            'date': date,	
            'time': time,	
            'exercise': exercise['user_input'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories'],
        }
    }
    sheets_response = requests.post(url=sheety_url, headers = sheety_headers, json=sheety_params, auth=(sheety_username,sheety_password))
