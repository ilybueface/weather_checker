import requests

city = input("City: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)

data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(weather_url)
data_too = response.json()

temperature = data_too["current_weather"]["temperature"]
wind_speed = data_too["current_weather"]["windspeed"]

print(f"In {city} is just {temperature} degrees C. and {wind_speed} km/h.")