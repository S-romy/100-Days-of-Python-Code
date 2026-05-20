import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": stock_api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()
time_series = data["Time Series (Daily)"]

closing_prices = [value["4. close"] for (key, value) in time_series.items()]
yesterday_price = float(closing_prices[0])

day_before_yesterday_price = float(closing_prices[1])

difference = yesterday_price - day_before_yesterday_price
percentage_difference = difference / day_before_yesterday_price * 100

required = {
    "apikey": news_api_key,
    "q": COMPANY_NAME,
    "language": "en"
}

response = requests.get(url=NEWS_ENDPOINT, params=required)
info = response.json()

news = info["articles"][:3]

if percentage_difference > 0:
    percent = "🔺"
else:
    percent = "🔻"


absolute_percentage = round(abs(percentage_difference))

news_list = [(f"{STOCK_NAME}: {percent}{absolute_percentage}% \nHeadline: {new['title']} \nBrief: {new['description']} "
              f"\nRead More: {new['url']}") for new in news]

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    receiver_address = email
    for item in news_list:
        message = f"Subject: Stock Alert!\n\n{item}"
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver_address,
            msg=message.encode("utf-8")
        )
