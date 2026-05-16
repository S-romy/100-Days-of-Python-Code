
from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

weather_api = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

MY_LAT = 9.076479
MY_LONG = 7.398574

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=weather_api, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if condition_data < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_ ='+17752528415',
        to='+2349022232315'
    )

    print(message.status)
