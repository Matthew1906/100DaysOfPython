from random import choice
import datetime as dt
import smtplib

email = 'email'
recipient_email = 'email'
password = 'password'

now = dt.datetime.now()

day_of_week = now.weekday()

print(day_of_week)
if day_of_week == 5:
    with open("Send Quotes/quotes.txt") as quote_file:
        quotes = quote_file.read().split("\n")
    quote = choice(quotes)
    quote = quote.split(" - ")
    message = "Subject: Saturday Quote of the Day\n\n" + "\n\n".join(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr=email, to_addrs=recipient_email, msg=message)
