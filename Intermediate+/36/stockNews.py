# 1. Import Modules
import requests, datetime as dt, smtplib

# 2. Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# 3. Get Yesterday and Day Before Yesterday Date
def format_num(month):
    if month<10:
        return f"0{month}"
    return month

def decode_string(message):
  return message.replace('\\xe2\\x80\\x99', "'").replace('\\xc3\\xa9', 'e').replace('\\xe2\\x80\\x90', '-').replace('\\xe2\\x80\\x91', '-').replace('\\xe2\\x80\\x92', '-').replace('\\xe2\\x80\\x93', '-').replace('\\xe2\\x80\\x94', '-').replace('\\xe2\\x80\\x94', '-').replace('\\xe2\\x80\\x98', "'").replace('\\xe2\\x80\\x9b', "'").replace('\\xe2\\x80\\x9c', '"').replace('\\xe2\\x80\\x9c', '"').replace('\\xe2\\x80\\x9d', '"').replace('\\xe2\\x80\\x9e', '"').replace('\\xe2\\x80\\x9f', '"').replace('\\xe2\\x80\\xa6', '...').replace('\\xe2\\x80\\xb2', "'").replace('\\xe2\\x80\\xb3', "'").replace('\\xe2\\x80\\xb4', "'").replace('\\xe2\\x80\\xb5', "'").replace('\\xe2\\x80\\xb6', "'").replace('\\xe2\\x80\\xb7', "'").replace('\\xe2\\x81\\xba', "+").replace('\\xe2\\x81\\xbb', "-").replace('\\xe2\\x81\\xbc', "=").replace('\\xe2\\x81\\xbd', "(").replace('\\xe2\\x81\\xbe', ")")

# Yesterday
yesterday = dt.datetime.today() - dt.timedelta(days=1)
yesterday = f'{yesterday.year}-{format_num(yesterday.month)}-{format_num(yesterday.day)}' 

# Day before Yesterday
day_before_yesterday = dt.datetime.today() - dt.timedelta(days=2)
day_before_yesterday = f'{day_before_yesterday.year}-{format_num(day_before_yesterday.month)}-{format_num(day_before_yesterday.day)}' 

# API Data, Parameters, Email data
# The API Key belongs to a dummy account, so i guess its fine to be shown to others (not my problem anyway)

stock_url = 'https://www.alphavantage.co/query'
stock_params={
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':STOCK,
    'apikey':'3Z2SH98M2V6RZ5EE'
}

news_api_url = 'https://newsapi.org/v2/everything'  
news_params = {        
    'q':COMPANY_NAME,
    'sortBy':'publishedAt',
    'apiKey': 'daff07e33d7044ff9d3530576c2cb670'
}

print("Input your credentials! (make sure it's gmail and you have allowed third party application to send emails")
user_mail = input("Insert your email: ")
user_pass = input("Insert your password: ")

# Analyze stock data
stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()
stock_response = stock_response.json()['Time Series (Daily)']

# Get Stock Data for yesterday and the day before yesterday
y_stock = float(stock_response[yesterday]['4. close'])
dby_stock = float(stock_response[day_before_yesterday]['4. close'])

stock_diff = (abs(y_stock-dby_stock)/dby_stock)*100

# 5. Get 3 newest news pieces for the company
# Errors might happen due to encoding issues
if stock_diff>=5:
    news_responses = requests.get(url=news_api_url, params=news_params)
    news_responses.raise_for_status()
    news_responses = news_responses.json()['articles'][:3]
# 6. Send 3 Separate Emails
    for news_response in news_responses:
        # The email has some weird symbols due to its encoding
        news_title = ''.join(news_response['title']).encode('utf-8')
        news_description = ''.join(news_response['description']).encode('utf-8')
        news_mail = decode_string(f"Subject: {news_title}\n\n{news_description}\n")
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user = user_mail , password= user_pass)
            connection.sendmail(from_addr= user_mail, to_addrs=user_mail, msg=news_mail)
        print(f'Email sent:\n{news_mail}\n')

