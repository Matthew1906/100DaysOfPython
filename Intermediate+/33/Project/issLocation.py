# Import modules
import requests, datetime as dt, time, smtplib

# Location of Jakarta
my_location={
    'lat':-6.175110,
    'long':106.865036, 
    'formatted':0
}

print("Input your credentials! (make sure it's gmail and you have allowed third party application to send emails")
user = input("Insert your email: ")
password = input("Insert your password: ")

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
        with smtplib.SMTP('smtp.gmail.com:587') as connection:
            connection.starttls()
            connection.login(user = user, password = password)
            connection.sendmail(from_addr=user, to_addrs=user, msg = 'Subject: Look Up!!\n\nYou might be able to see the International Space Station\n\nHeads up!!')
    else:
      print("Not even close")

# Supposedly notify every 30 minutes with an email if International Space Station is close (if its not it won't send an email), can just be run on python anywhere with an interval

while True:
    iss_inform()
    time.sleep(1800)
