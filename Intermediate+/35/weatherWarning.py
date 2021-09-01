# Import modules
import requests, smtplib

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

print("Input your credentials! (make sure it's gmail and you have allowed third party application to send emails")
user = input("Insert your email: ")
password = input("Insert your password: ")
print("This program will send an email from your own email to your email, notifying you about the weather. I made it like that so anyone can use them without environment restrictions")

if will_rain:
    message = 'Subject:Hello there, Weather Alert\n\nIt will rain today, bring an umbrella!'
else:
    message = "Subject:Hello there, Weather Alert\n\nIt might not rain today, but bring an umbrella just in case!"

with smtplib.SMTP("smtp.gmail.com:587") as connection:
    connection.starttls()
    connection.login(user = user, password=password)
    connection.sendmail(from_addr=user, to_addrs=user, msg=message)
