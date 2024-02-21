from pprint import pprint
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK_DATA= 'CP6LNZWNUIAVAENM'
API_KEY_NEWS_DATA = '28a2e7e746684c869d144bf9c95014af'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'AC5dec45cb5a0c6e55f07d37f2280f1a4a'                   # for twilio
auth_token = '7b8e8b510589078763536dc097c33f7c'

# PARAMTERS FOR STOCK DATA API
paramaters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':API_KEY_STOCK_DATA,
    'outputsize':'compact'
}

#Use https://newsapi.org/docs/endpoints/everything
response = requests.get(url=STOCK_ENDPOINT, params=paramaters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]         # because taping into the dates is easier by using list
yesterday_close = (data_list[0]['4. close'])
day_before_yesterday_close = (data_list[1]['4. close'])
difference = abs(float(yesterday_close) - float(day_before_yesterday_close))
percentage_change = round((difference/float(day_before_yesterday_close))*100, 3)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

if percentage_change > 2:
    news_params = {
        'apikey':API_KEY_NEWS_DATA,
        'qInTitle':COMPANY_NAME

    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()['articles']
    three_articles = news_data[:3]
    formatted_articles = [f"{STOCK}: {percentage_change}% \n headlines: {article['title']} . \n Brief:{article['description']} " for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            from_='+14015371051',
            body=article,
            to='+919373440165'
        )
        print(message.status)
