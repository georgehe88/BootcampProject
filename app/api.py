#app/api.py

import requests
# from app.models import get_external_data

class PirateWeatherAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.pirateweather.net/forecast/"
        self.api_key = api_key

    def get_weather_by_city(self, city_name):
        url = f"{self.base_url}{self.api_key}/{city_name}"
        return self._make_request(url)

    def get_weather_by_zip(self, zip_code):
        url = f"{self.base_url}{self.api_key}/{zip_code}"
        return self._make_request(url)

    def get_weather_by_coordinates(self, latitude, longitude):
        url = f"{self.base_url}{self.api_key}/{latitude},{longitude}"
        return self._make_request(url)

    def _make_request(self, url):
        response = requests.get(url)
        return response.json()

    def get_external_data():
        url = "https://api.external.com/data"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
