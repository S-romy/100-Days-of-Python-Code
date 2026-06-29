import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

WEIGHT_KG = float(os.getenv("WEIGHT"))
HEIGHT_CM = float(os.getenv("HEIGHT"))
AGE_YRS = int(os.getenv("AGE"))
GENDER = os.getenv("SEX")

API_KEY = os.getenv("EXERCISE_API_KEY")
APP_ID = os.getenv("EXERCISE_APP_ID")
SHEETY_TOKEN = os.getenv("TOKEN")
BASE_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

user_params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE_YRS,
    "gender": GENDER
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=BASE_URL, json=user_params, headers=headers)
result = response.json()["exercises"]

SHEETY_ENDPOINT = "https://api.sheety.co/f2828a894742fb3a49563d1be688152d/myWorkouts/sheet1"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")


for exercise in result:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(f"Status Code: {sheety_response.status_code}")
    print(sheety_response.text)
