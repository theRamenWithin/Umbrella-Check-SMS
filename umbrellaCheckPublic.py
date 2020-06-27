#! python3
# umbrellaCheck.py - Checks weather service to see if I need an umbrella today
# and sends me a message over WhatsApp

import json
import requests
from twilio.rest import Client

# Set message to be sent to WhatsApp to an empty list.
messageSMS = []
mAp = messageSMS.append

# Preset values:
accountSID = # accountSID goes here
authToken = # authToken goes here
myNumber = # my mobile number 
twilioNumber = # my twilio phone number


def textMyself(message):
    client = Client(accountSID, authToken)
    client.messages.create(from_=twilioNumber, body=message, to=myNumber)


# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/onecall?lat=-33&lon=151&units=metric&appid=%s' % authToken 
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Checks the tempature and main weather condition for the day and appends the
# WhatsApp message it directions accordingly
w = weatherData['daily'][0]
if w['temp']['day'] < 15:
    mAp('Bring a jacket, it will be ' + str(w['temp']['day']) + 'C today.')
if w['weather'][0]['main'] == 'Rain' or w['weather'][0]['main'] == 'Snow':
    mAp('Bring an umbrella.')

if messageSMS == []:
    exit()
else:
    textMyself(' '.join(messageSMS))
