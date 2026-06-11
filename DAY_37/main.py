import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
ID = os.getenv("PIXELA_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": ID,
    "name": "Code Tracking Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)

code_tracker_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.now()

code_tracker_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?: ")
}

response = requests.post(url=code_tracker_endpoint, json=code_tracker_config, headers=header)
print(response.text)

update_endpoint = f"{code_tracker_endpoint}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "6"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=header)
# print(response.text)

delete_endpoint = f"{code_tracker_endpoint}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
