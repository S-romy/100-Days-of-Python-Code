import requests
import os
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.serp_api_key = os.getenv("SERP_API_KEY")
        self.serp_endpoint = "https://serpapi.com/search"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self.serp_api_key,
        }

        serp_api_response = requests.get(url=self.serp_endpoint, params=params)

        if serp_api_response.status_code != 200:
            print(f"check_flights() response code: {serp_api_response.status_code}")
            print(serp_api_response.text)
            return None
        else:
            data = serp_api_response.json()

            if "error" in data:
                print(f"API error: {data['error']}")
                return None
            return data
