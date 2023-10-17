#October 16, 2023

import smtplib
import datetime as dt
import random

MY_EMAIL = "example1@gmail.com"
MY_PASSWORD = "password123"
RECIPIENT_EMAIL = "example2@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("day032/MondayMotivator/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        todays_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=RECIPIENT_EMAIL, 
            msg=f"Subject:Monday Motivation\n\n{todays_quote}")
        connection.close()