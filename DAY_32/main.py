import random
import smtplib
import pandas
import datetime as dt

# Extra Hard Starting Project #
MY_EMAIL = "orahachi16@gmail.com"
PASSWORD = "something"

# 1. Update the birthdays.csv
letters = []
with open("letter_templates/letter_1.txt", mode="r") as letter_1:
    l1 = letter_1.read()
    letters.append(l1)
with open("letter_templates/letter_2.txt", mode="r") as letter_2:
    l2 = letter_2.read()
    letters.append(l2)
with open("letter_templates/letter_3.txt", mode="r") as letter_3:
    l3 = letter_3.read()
    letters.append(l3)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)

data = pandas.read_csv("birthdays.csv")
new_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
if today in new_dict:
    letter = random.choice(letters)
    word = "[NAME]"
    name = new_dict[today]["name"]
    new_letter = letter.replace(word, name)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        receiver_address = new_dict[today]["email"]
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=receiver_address,
            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )
