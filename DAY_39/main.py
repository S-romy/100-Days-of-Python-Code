# imports
import requests_cache
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta

# cache setup
requests_cache.install_cache(
    "flight_cache",
    expire_after=3600
)

# date setup
today = datetime.now()
tomorrow = (today + timedelta(days=1)).strftime("%Y-%m-%d")
next_six_months = (today + timedelta(days=180)).strftime("%Y-%m-%d")

# Sheety test
datamanager = DataManager()
sheet_data = datamanager.get_destination_data()
pprint(sheet_data)

# SerpAPI flight test
flight_search = FlightSearch()

# Use twilio to send a message
notification_manager = NotificationManager()

for destination in sheet_data:
    print(f"Searching flights to {destination['city']}...")
    flight_search_response = flight_search.check_flights(origin_city_code="ABV",
                                                         destination_city_code=destination["iataCode"],
                                                         from_time=tomorrow, to_time=next_six_months)
    if flight_search_response is None:
        continue
    else:
        pprint(flight_search_response)

    cheapest_flight = find_cheapest_flight(flight_search_response, next_six_months)

    if cheapest_flight.price == "N/A":
        continue
    print(cheapest_flight.price)
    print(f"New price: {cheapest_flight.price}, saved price: {destination['lowestPrice']}")

    if cheapest_flight.price <= destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        datamanager.update_lowest_price(
            row_id=destination["id"],
            new_price=cheapest_flight.price,
        )

        notification_manager.send_sms(
            f"Low price alert! Only ${cheapest_flight.price}\n"
            f"From Abuja — {cheapest_flight.origin_airport_name} "
            f"({cheapest_flight.origin_airport})\n"
            f"To {destination['city']} — {cheapest_flight.destination_airport_name} "
            f"({cheapest_flight.destination_airport})\n"
            f"Outbound: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )
