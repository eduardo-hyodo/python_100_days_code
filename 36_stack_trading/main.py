import requests
from datetime import date, timedelta
from decimal import Decimal
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"


def get_stock_price(stock_api_params):
    r = requests.get(STOCK_API_URL, params=stock_api_params)
    data = r.json()
    daily_series = data["Time Series (Daily)"]
    # instead, could be  daily_series = [value for (key,value) in data["Time Series (Daily)"].items
    return daily_series


def get_news(url, news_api_key):
    news_api_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": news_api_key,
        "language": "en",
        "pageSize": 3,
    }
    r = requests.get(url, params=news_api_params)
    news = r.json()["articles"]
    return news


def send_news(twilio_params, news, percentage_delta):
    for new in news:
        client = Client(twilio_params["account_sid"], twilio_params["auth_token"])
        message = client.messages.create(
            from_=twilio_params["from_cellphone"],
            body=f"{COMPANY_NAME}:{percentage_delta}\nHeadline:{new['title']}\nBrief:{new['description']}",
            to=twilio_params["to_cellphone"],
        )
        print(message.sid)


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases
# by 5% between yesterday and the day before yesterday then print("Get News").
with open("data.txt") as access:
    stock_api_key = access.readline().rstrip()
    news_api_key = access.readline().rstrip()
    twilio_account_sid = access.readline().rstrip()
    twilio_auth_token = access.readline().rstrip()
    from_cellphone = access.readline().rstrip()
    to_cellphone = access.readline().rstrip()

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}


stock_price_per_day = get_stock_price(stock_api_params)
yesterday = str(date.today() - timedelta(days=1))
day_before_yesterday = str(date.today() - timedelta(days=2))
close_price_yesteday = Decimal(stock_price_per_day[yesterday]["4. close"])
close_price_day_before_yesteday = Decimal(
    stock_price_per_day[day_before_yesterday]["4. close"]
)
delta = close_price_yesteday - close_price_day_before_yesteday
percentage_delta = round(((delta * 100) / close_price_yesteday), 2)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"),
# actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change
# and each article's title and description to your phone number.

if abs(percentage_delta) > 5:
    news = get_news(NEWS_API_URL, news_api_key)

    twilio_params = {
        "account_sid": twilio_account_sid,
        "auth_token": twilio_auth_token,
        "from_cellphone": from_cellphone,
        "to_cellphone": to_cellphone,
    }
    send_news(twilio_params, news, percentage_delta)


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
# and prominent investors are required to file by the SEC The 13F filings show
# the funds' and investors' portfolio positions as of March 31st, near the
# height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings
# that hedge funds and prominent investors are required to file
# by the SEC The 13F filings show the funds' and investors' portfolio
# positions as of March 31st, near the height of the coronavirus market crash.
# """
