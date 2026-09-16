import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.basic_authentication = os.getenv("SHEETY_BASIC_AUTHENTICATION")
        self.prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.header = {"Authorization": f"Basic {self.basic_authentication}"}
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=self.prices_endpoint, headers=self.header)
        sheety_data = sheety_response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        endpoint = f"{self.prices_endpoint}/{row_id}"

        body = {
            "price": {
                "lowestPrice": new_price
            }
        }

        response = requests.put(
            url=endpoint,
            json=body,
            headers=self.header,
        )

        print(response.status_code)
        print(response.text)
        response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(
            url=self.users_endpoint,
            headers=self.header,
        )
        response.raise_for_status()
        return response.json()["users"]
