import os
import requests
import json

from utils import get_OpenWeatherAPI_token


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
    response = rq.text
    return response


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
    response = rq.text
    return response