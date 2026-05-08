import requests
import smtplib
import time
from datetime import datetime


MY_EMAIL = "orahachi16@gmail.com"
PASSWORD = "something"

MY_LAT = 9.076479
MY_LONG = 7.398574


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    # Your position within -5 or +5 degrees of the ISS.
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True
    return False


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    print("Checking ISS...")
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        print("ISS is overhead! Sending alert...")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            receiver_address = MY_EMAIL
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=receiver_address,
                msg=f"Subject:Look up!\n\nThe ISS is above you in the sky."
            )
