from flask import Flask, jsonify, render_template, request
from geopy.geocoders import Nominatim
import requests

app = Flask(__name__)

BASE_URL = "https://api.pirateweather.net/forecast/"
API_KEY = "9Pn8CfvVbD6NaHdukQWoo0T5MaFGXwVJ"

# Function to get weather data based on location input
def get_weather_data(location_input):
    try:
        # Function to get latitude and longitude from location input
        def get_coordinates(location):
            try:
                # If the input is already latitude and longitude, split and return
                if ',' in location:
                    latitude, longitude = location.split(',')
                    return latitude.strip(), longitude.strip()

                # If the input is a city name or zipcode, use geocoding to get coordinates
                geolocator = Nominatim(user_agent="weather_app")
                location = geolocator.geocode(location)
                if location:
                    return str(location.latitude), str(location.longitude)
                else:
                    print("Location not found")
                    return None, None
            except Exception as e:
                print(f"Error occurred while getting coordinates: {e}")
                return None, None

        # Get latitude and longitude from the location input
        latitude, longitude = get_coordinates(location_input)
        if latitude is not None and longitude is not None:
            # Construct the URL based on the location and API key
            location = f"{latitude},{longitude}"
            url = f"{BASE_URL}{API_KEY}/{location}?exclude=minutely,daily&extend=hourly&tz=auto"

            # Send the request and get the response
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            response.raise_for_status()

            # Parse JSON response
            weather_data = response.json()
            return weather_data
        else:
            return None
    except requests.exceptions.RequestException as e:
        # Print error message if request was not successful
        print(f"HTTP error occurred: {e}")
        return None

# Route to render the weather page
@app.route('/')
def weather_page():
    return render_template('weather6.html')

# Route to handle form submission and fetch weather data
@app.route('/get_weather', methods=['POST'])
def fetch_weather():
    location_input = request.form['location']
    weather_data = get_weather_data(location_input)

    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Weather data not available'})

if __name__ == '__main__':
    app.run(debug=True)
