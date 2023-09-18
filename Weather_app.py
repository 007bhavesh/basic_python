import requests
import json
import os

city = input("Enter the name of the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=7bb1c4fc1f67464c89c115908231508&q={city}"

r = requests.get(url)
print(r.text)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(wdic["current"]["temp_c"])

os.system(f"say 'The current temperature in {city} is {w} degrees'")