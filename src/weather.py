import os
import requests
import json

from constants import WEATHER_GROUP_GOOD_WEATHER
from utils import get_OpenWeatherAPI_token


def obtain_weather_from_response(response):
    """Method that gets the OpenWeather response and returns the part corresponding to the weather"""

    # Deserializing the JSON text
    json_text = json.loads(response.text)

    # Getting the weather
    weather_key = 'weather'
    weather = json_text[weather_key][0]  # Weather is a 1-element array

    return weather


def get_current_weather_in_city(city):
    """Method that gets the current weather for the specified city

    The weather is returned in JSON format. More info about the responses can be found in the official API call
    documentation site (http://openweathermap.org/current)"""

    TOKEN = get_OpenWeatherAPI_token()

    # Asking for the weather
    current_weather_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {'appid': TOKEN, 'q': city}
    rq = requests.get(current_weather_URL, params=params)

    # Returning the weather
    weather = obtain_weather_from_response(rq)
    return weather


def get_current_weather_in_location(location):
    """Method that gets the current weather for the specified Telegram Location

    The weather is returned in JSON format. More info about the responses can be found in the official API call
    documentation site (http://openweathermap.org/current)"""

    TOKEN = get_OpenWeatherAPI_token()

    # Getting longitude and latitude from location
    lon = location.location.longitude
    lat = location.location.latitude

    # Asking for the weather
    current_weather_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {'appid': TOKEN, 'lon':lon, 'lat':lat}
    rq = requests.get(current_weather_URL, params=params)

    # Returning the weather
    weather = obtain_weather_from_response(rq)
    return weather