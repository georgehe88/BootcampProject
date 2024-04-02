from app import app
from app.api import PirateWeatherAPI

if __name__ == "__main__":
    app.run(debug=True)
    api_key = "DtO2mxqpPQNuEmVg2yugXkZ9eWRg3fLk"
    weather_api = PirateWeatherAPI(api_key)

    # Search by city
    city_name = "New York"
    city_weather = weather_api.get_weather_by_city(city_name)
    print(f"Weather in {city_name}: {city_weather}")

    # Search by zip code
    zip_code = "10001"
    zip_weather = weather_api.get_weather_by_zip(zip_code)
    print(f"Weather in {zip_code}: {zip_weather}")

    # Search by coordinates
    latitude = 40.7128
    longitude = -74.0060
    coordinates_weather = weather_api.get_weather_by_coordinates(latitude, longitude)
    print(f"Weather at coordinates ({latitude}, {longitude}): {coordinates_weather}")

     