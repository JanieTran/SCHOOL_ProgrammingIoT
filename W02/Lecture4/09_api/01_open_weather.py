# Documentation: https://openweathermap.org/current
import requests
import json

# APPID = "b6907d289e10d714a6e88b30761fae22" # Sample API Key.
APPID = "01f8a6161032a97ce8113b1fe410a749"  # Real API Key.

response = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q={city},{countryCode}&appid={appid}".format(
        city="Melbourne", countryCode="au", appid=APPID))

data = json.loads(response.text)
print(json.dumps(data, indent=4))
