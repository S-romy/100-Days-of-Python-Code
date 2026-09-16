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

customer_data = datamanager.get_customer_emails()

customer_emails = [
    customer["whatIsYourEmailAddress?"]
    for customer in customer_data
]

print(customer_emails)

# SerpAPI flight test
flight_search = FlightSearch()

# Use twilio to send a message
notification_manager = NotificationManager()

for destination in sheet_data:
    print(f"Searching direct flights to {destination['city']}...")
    flight_search_response = flight_search.check_flights(origin_city_code="ABV",
                                                         destination_city_code=destination["iataCode"],
                                                         from_time=tomorrow, to_time=next_six_months)
    if flight_search_response is None:
        continue
    else:
        pprint(flight_search_response)

    cheapest_flight = find_cheapest_flight(flight_search_response, next_six_months)

    if cheapest_flight.price == "N/A":
        print(
            f"No direct flight to {destination['city']}. "
            "Looking for indirect flights..."
        )
        flight_search_response = flight_search.check_flights(
            origin_city_code="ABV",
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=next_six_months,
            is_direct=False,
        )

        if flight_search_response is None:
            continue

        cheapest_flight = find_cheapest_flight(
            flight_search_response,
            next_six_months,
        )

    if cheapest_flight.price == "N/A":
        print(f"No flights found to {destination['city']}.")
        continue

    print(
        f"Cheapest flight to {destination['city']}: "
        f"${cheapest_flight.price} — {cheapest_flight.stops} stop(s)"
    )

    if cheapest_flight.price <= destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        datamanager.update_lowest_price(
            row_id=destination["id"],
            new_price=cheapest_flight.price,
        )

        if cheapest_flight.stops == 0:
            email_body = (
                f"Low price alert! Only ${cheapest_flight.price} to "
                f"{destination['city']}.\n\n"
                f"Airline: {cheapest_flight.airline}.\n"
                "This is a direct flight.\n\n"
                f"From: {cheapest_flight.origin_airport_name} "
                f"({cheapest_flight.origin_airport}).\n"
                f"To: {cheapest_flight.destination_airport_name} "
                f"({cheapest_flight.destination_airport}).\n"
                f"Outbound: {cheapest_flight.out_date}\n"
                f"Return: {cheapest_flight.return_date}"
            )
        else:
            email_body = (
                f"Low price alert! Only ${cheapest_flight.price} to "
                f"{destination['city']}.\n\n"
                f"Airline: {cheapest_flight.airline}.\n"
                f"This flight has {cheapest_flight.stops} stop.\n"
                f"Stopover: {cheapest_flight.layover_location}.\n\n"
                f"From: {cheapest_flight.origin_airport_name} "
                f"({cheapest_flight.origin_airport}).\n"
                f"To: {cheapest_flight.destination_airport_name} "
                f"({cheapest_flight.destination_airport}).\n"
                f"Outbound: {cheapest_flight.out_date}\n"
                f"Return: {cheapest_flight.return_date}"
            )

        notification_manager.send_emails(
            email_list=customer_emails,
            email_body=email_body,
        )
