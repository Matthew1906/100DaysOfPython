# DAY 35 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: Weather Warning 
# THINGS I IMPLEMENTED: SMTPLIB, API Authentication, REQUESTS, JSONS

import requests, smtplib

# Other types of data that are valuable
# People charge for API, because it is quite hard to get the data
# API = selling data 


weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
weather_params= {
    'lat':-6.175110,
    'lon':106.865036,
    'exclude':'current,minutely,daily,alerts',
    'appid':'69f04e4613056b159c2761a9d9e664d2' # its not my api id
}

weather_response = requests.get(url=weather_url, params=weather_params)
weather_response.raise_for_status()
weathers = weather_response.json()['hourly'][:12]

will_rain = False
for idx in range(12):
    if weathers[idx]['weather'][0]['id']<700:
        will_rain = True
        break

# We can use TWILIO API to send sms, but i am not using it duh

user = 'user@mail.com'
recipient = 'recipient@mail.com'
password = 'a1b2c3d4e5f6g7h8i9j0k'

if will_rain:
    message = 'Subject:Hello there, Weather Alert\n\nIt will rain today, bring an umbrella!'
else:
    message = "Subject:Hello there, Weather Alert\n\nIt might not rain today, but bring an umbrella just in case!"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = user, password=password)
    connection.sendmail(from_addr=user, to_addrs=recipient, msg=message)


