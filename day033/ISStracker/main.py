# Bilal Mirza
# November 7, 2023
# First time utilizing the "requests" import to practice using the 
# International Space Station's public API provided by Open Notify

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(f"The International Space Station's Current Location is " + str(iss_position))