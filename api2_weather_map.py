# File: api2_weather_map.py
# Description: Conceptual demonstration of how to use the OpenWeatherMap API with Python's requests library.

# Import the 'requests' library to make HTTP calls.
# Official Docs: https://docs.python-requests.org/en/latest/
import requests

# What is OpenWeatherMap API?
# ---------------------------
# OpenWeatherMap provides weather data through APIs.
# It requires a free API key, which you can get by registering here:
# Link: https://openweathermap.org/api

# API keys are used to track and limit API usage per user (for security and fair use).
# You'll need to insert your personal API key in the URL when making a request.


# Let's build a sample GET request step by step:
# ----------------------------------------------

# Step 1: Choose a city (example: Toronto)
city = "Toronto"

# Step 2: Your unique API key (replace with your actual key after signing up)
api_key = "your_api_key_here"

# Step 3: Define the base URL (this endpoint gives current weather data by city name)
# Docs: https://openweathermap.org/current
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Step 4: Create a full URL with query parameters (city name, API key, units)
# Tip: `units=metric` will return temperature in Celsius
url = f"{base_url}?q={city}&appid={api_key}&units=metric"

# Step 5: Make the GET request
response = requests.get(url)

# Step 6: Check for success and handle the data
if response.status_code == 200:
    # Convert JSON response to Python dictionary
    data = response.json()

    # Print the entire data for inspection
    print("Full API response:\n", data)

    # Extract and display a few useful fields
    temperature = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print("\nWeather Details:")
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Description: {weather_desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("Failed to retrieve weather data. Status code:", response.status_code)

# Tips:
# -----
# > If you get a 401 error, check if your API key is correct or activated.
# > Always inspect the returned JSON structure before coding – use print(data) to explore.
# > For more weather data (like forecasts, air pollution), check other endpoints:
#   Docs: https://openweathermap.org/api
