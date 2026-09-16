import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.basic_authentication = os.getenv("SHEETY_BASIC_AUTHENTICATION")
        self.sheety_endpoint = "https://api.sheety.co/f2828a894742fb3a49563d1be688152d/flightDeals/sheet1"
        self.header = {"Authorization": f"Basic {self.basic_authentication}"}
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=self.sheety_endpoint, headers=self.header)
        sheety_data = sheety_response.json()
        self.destination_data = sheety_data["sheet1"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        endpoint = f"{self.sheety_endpoint}/{row_id}"

        body = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }

        requests.put(
            url=endpoint,
            json=body,
            headers=self.header,
        )
