import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(
                user=self.email,
                password=self.password,
            )

            for customer_email in email_list:
                print(f"Sending email to: {customer_email}")
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=customer_email,
                    msg=(
                        f"Subject: The Flight Club!\n\n"
                        f"{email_body}"
                    ).encode("utf-8"),
                )
