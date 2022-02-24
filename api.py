from urllib import response
import requests

API_KEY = "1a9ffd23ddmshccf77501a944e81p1a5578jsn14a6bbe459bb"
BASE_URL = "https://community-open-weather-map.p.rapidapi.com/weather"

city = input("Enter the city:")

REQUEST_URL = f"{BASE_URL}?apiid={API_KEY}&q={city}"

response = requests.get(REQUEST_URL)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred")