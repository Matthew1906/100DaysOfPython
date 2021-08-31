# DAY 33 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: ISS Location + Nighttime Detector
# THINGS I IMPLEMENTED: SMTPLIB, API, DATETIME, REQUESTS, JSON

import requests, datetime as dt, time, smtplib

# Location of Jakarta
my_location={
    'lat':-6.175110,
    'long':106.865036, 
    'formatted':0
}

user = 'sender@mail.com'
password = 'password'
recipient = 'recipient@mail.com'

def is_close():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    location = response.json()['iss_position']
    latitude = float(location['latitude'])
    longitude = float(location['longitude'])
    if abs(latitude-my_location['lat'])<=5 and abs(longitude-my_location['long'])<=5:
        return True
    return False

def is_night():
    sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'
    sun_response = requests.get(url = sunrise_sunset_api, params=my_location)
    sun_response.raise_for_status()
    sunrise = sun_response.json()['results']['sunrise'].split("T")[-1].split(":")[0]
    sunset = sun_response.json()['results']['sunset'].split("T")[-1].split(":")[0]
    now = dt.datetime.now().hour
    if now>=sunset or now<=sunrise:
        return True
    return False

def iss_inform():
    if is_close() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user = user, password = password)
            connection.sendmail(from_addr=user, to_addrs=recipient, msg = 'Subject: Look Up!!\n\nYou might be able to see the International Space Station\n\nHeads up!!')

while True:
    time.sleep(1800)
    iss_inform()
