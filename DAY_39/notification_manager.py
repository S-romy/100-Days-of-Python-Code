import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")

    def send_sms(self, info):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=info,
            from_=self.virtual_number,
            to=self.verified_number
        )

