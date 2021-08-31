# DAY 36 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: STOCK TRADING MESSAGE APP
# THINGS I IMPLEMENTED: SMTPLIB, API, DATETIME, REQUESTS, JSON

# Import Modules
import requests, datetime as dt, smtplib

# 2. Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# 3. Get Yesterday and Day Before Yesterday Date
def format_num(month):
    if month<10:
        return f"0{month}"
    return month

# Yesterday
yesterday = dt.datetime.today() - dt.timedelta(days=1)
yesterday = f'{yesterday.year}-{format_num(yesterday.month)}-{format_num(yesterday.day)}' 

# Day before Yesterday
day_before_yesterday = dt.datetime.today() - dt.timedelta(days=2)
day_before_yesterday = f'{day_before_yesterday.year}-{format_num(day_before_yesterday.month)}-{format_num(day_before_yesterday.day)}' 

# API Data, Parameters, Email data
stock_url = 'https://www.alphavantage.co/query'
stock_params={
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':STOCK,
    'apikey':'APIKEY'
}

news_api_url = 'https://newsapi.org/v2/everything'  
news_params = {        
    'q':COMPANY_NAME,
    'sortBy':'publishedAt',
    'apiKey':'APIKEY'
}

user_mail = 'user@mail.com'
user_pass = 'password'
recipient_mail = 'recipient@mail.com'

## 4. Analyze Stock Data: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday
stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()
stock_response = stock_response.json()['Time Series (Daily)']

# Get Stock Data for yesterday and the day before yesterday
y_stock = float(stock_response[yesterday]['4. close'])
dby_stock = float(stock_response[day_before_yesterday]['4. close'])

stock_diff = (abs(y_stock-dby_stock)/dby_stock)*100

## 5. Get 3 news pieces for the COMPANY_NAME: Use https://newsapi.org
if stock_diff<=5:
    # Get the first 3 news pieces for the COMPANY_NAME
    news_responses = requests.get(url=news_api_url, params=news_params)
    news_responses.raise_for_status()
    news_responses = news_responses.json()['articles'][:3]
# 6. Send 3 Separate Emails
    for news_response in news_responses:
        news_title = news_response['title']
        news_description = news_response['description']
        # Can't send email because it can't be encoded
        news_mail = f"Subject: {news_title}\n\n{news_description}\n"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = user_mail , password= user_pass)
            connection.sendmail(from_addr= user_mail, to_addrs=recipient_mail, msg=news_mail)
