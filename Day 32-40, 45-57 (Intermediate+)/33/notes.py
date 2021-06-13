import requests
import datetime as dt

# get what's inside
response = requests.get(url='http://api.open-notify.org/iss-now.json')

# Check status
response.raise_for_status()

# Get json data
location = response.json()['iss_position']
iss_position = (location['latitude'],location['longitude'])
print(iss_position)

# link to check langitude longitude: https://www.latlong.net/

# Get sunrise and sunset time

location_parameter ={
    'lat':-6.175110,
    'lng':106.865036,
    'formatted':0
}

sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'
sun_response = requests.get(url = sunrise_sunset_api, params=location_parameter)
sun_response.raise_for_status()

sunrise = sun_response.json()['results']['sunrise'].split("T")[-1].split(":")[0]
sunset = sun_response.json()['results']['sunset'].split("T")[-1].split(":")[0]
now = dt.datetime.now().hour

# If the ISS is close to my current location, and it is currently dark, 
# send an email to inform me to look up, run the code every 60 seconds

