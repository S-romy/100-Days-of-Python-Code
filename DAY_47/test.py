import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = "https://appbrewery.github.io/instant_pot/"

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver_address = os.getenv("RECEIVER")

amazon_dummy_website = requests.get(url)
website_text = amazon_dummy_website.text
soup = BeautifulSoup(website_text, "html.parser")
whole_price = soup.find(name="span", class_="a-price-whole")
decimal_price = soup.find(name="span", class_="a-price-fraction")
price = float(whole_price.text + decimal_price.text)
target_price = 100.00

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver_address,
            msg=f"Subject:Instant Pot Price Alert\n\n"
                f"The Product Price is now ${price}, below your target price. Buy now!"
        )
    print("Message sent. Price is below your target amount.")
else:
    print("Message not sent. Price is not below the target amount.")
