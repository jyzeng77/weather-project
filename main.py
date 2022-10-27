import os
import requests 
import json

city = input("Enter a city: ")
key = str(os.environ['KEY'])

url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
location_call = json.loads(requests.get(url).content)

print(location_call)
lat = location_call[0]['lat']
lon = location_call[0]['lon']

print("Lat:",lat)
print("Lon:",lon)

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}"
weather_call = requests.get(url).content
weather_call = json.loads(weather_call)

print("Temperature:", weather_call["main"]["temp"])
