import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver_address = os.getenv("RECEIVER")
api_key = os.getenv("API_KEY")

amazon_url = "https://www.amazon.com/dp/B06Y1YD5W7?ref=clp_cat_related_p_0&th=1"
header = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "lc-main=en_US; i18n-prefs=USD"
}

amazon_website = requests.get(amazon_url, headers=header)
website_text = amazon_website.text
soup = BeautifulSoup(website_text, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
price = price.text.replace("$", "")
price = float(price)

target_price = 100.00

currency_url = "https://api.currencyfreaks.com/v2.0/rates/latest"
response = requests.get(
    currency_url,
    params={
        "apikey": api_key,
        "symbols": "NGN"
    }
)

data = response.json()
rate = float(data["rates"]["NGN"])

if price < target_price:
    naira = price * rate

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver_address,
            msg=f"Subject: Instant Pot Price Alert\n\n"
                f"The Product Price is now NGN {naira:,.2f}, below your target price. Buy now!"
        )
    print("Message sent. Price is below your target amount.")
else:
    print("Message not sent. Price is not below the target amount.")
