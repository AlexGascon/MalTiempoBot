import requests
import json

from constants import WEATHER_GROUP_GOOD_WEATHER
from utils import get_OpenWeatherAPI_token


def obtain_weather_from_api_response(response):
    """Method that gets the OpenWeather response and returns the part corresponding to the weather

    NOTE: Weather can be an array containing more than one weather condition"""

    # Deserializing the JSON text
    json_text = json.loads(response.text)

    # Getting the weather
    weather_key = 'weather'
    weather = json_text[weather_key]

    return weather


def is_bad_weather(weather):
    """Method that returns a boolean indicating if the weather is bad (rain, snow, thunderstorm...)"""
    return weather['id'] not in WEATHER_GROUP_GOOD_WEATHER


def get_current_weather_in_city(city):
    """Method that gets the current weather for the specified city

    The weather is returned in JSON format. More info about the responses can be found in the official API call
    documentation site (http://openweathermap.org/current)"""

    TOKEN = get_OpenWeatherAPI_token()

    # Asking for the weather
    current_weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'appid': TOKEN, 'q': city}
    rq = requests.get(current_weather_url, params=params)

    # Returning the weather
    weather = obtain_weather_from_api_response(rq)
    return weather


def get_current_weather_in_location(lat, lon):
    """Method that gets the current weather for the specified location

    The weather is returned in JSON format. More info about the responses can be found in the official API call
    documentation site (http://openweathermap.org/current)"""

    # Checking that the message contains actually a location
    if (lon, lat) == (-1, -1):
        return False  # Use a custom exception in the future

    TOKEN = get_OpenWeatherAPI_token()

    # Asking for the weather
    current_weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'appid': TOKEN, 'lon': lon, 'lat': lat}
    rq = requests.get(current_weather_url, params=params)

    # Returning the weather
    weather = obtain_weather_from_api_response(rq)
    return weather


def get_today_forecast_in_location(lat, lon):
    """Method that gets the current day forecast for the specified location. 
    
    As there isn't a direct request to obtain the current day forecast, what we'll do is to obtain the 5-day forecast
    and return only the predictions corresponding only to the following 24 hours. As the 5-day forecast returns the
    forecasts in 3 hour timeframes, we'll get the first 8. """

    return get_forecast_in_location(lat=lat, lon=lon, days=1)


def get_3day_forecast_in_location(lat, lon):
    """Method that gets a 3 day forecast for the specified location

    The weather is returned in JSON format. More info about the responses can be found in the official API call
    documentation site (http://openweathermap.org/current)"""

    return get_forecast_in_location(lat=lat, lon=lon, days=3)


def get_forecast_in_location(lat, lon, days=3):
    """Generic method to get the forecast in a specified location for a variable number of days

    The weather is returned in JSON format. More info about the responses can be found in the official API documentation
    site (http://openweathermap.org/current)"""

    # Checking that the message contains actually a location
    if (lon, lat) == (-1, -1):
        raise AttributeError  # Use a custom exception in the future

    TOKEN = get_OpenWeatherAPI_token()

    # Asking for the weather
    current_weather_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {'appid': TOKEN, 'lon': lon, 'lat': lat}
    rq = requests.get(current_weather_url, params=params)

    weathers = []
    # Deserializing the JSON text
    json_text = json.loads(rq.text)

    # Obtaining all the weather forecast in the 5-day range
    forecast_list = json_text['list']
    for forecast in forecast_list:
        for weather in forecast['weather']:
            weathers.append(weather)

    # Returning the weather
    # As the forecast returns the weather in 3-hours intervals, 8 items represent 24 hours (1 day)
    return weathers[:days*8]

def get_today_temperatures_in_location(lat, lon):
    """Returns an array with the min temperatures expected for the following 24 hours"""

    TOKEN = get_OpenWeatherAPI_token()

    # Asking for the weather
    current_weather_URL = "http://api.openweathermap.org/data/2.5/forecast"
    params = {'appid': TOKEN, 'lon': lon, 'lat': lat}
    rq = requests.get(current_weather_URL, params=params)

    # Deserializing the JSON text
    json_text = json.loads(rq.text)

    # Obtaining all the weather forecast in the 5-day range
    min_temperatures = []
    forecast_list = json_text['list']
    for forecast in forecast_list:
        # The temperature is in Kelvin, so we'll convert it to Celsius
        min_temp_kelvin = float(forecast['main']['temp_min'])
        min_temperatures.append(min_temp_kelvin - 273.15)

    return min_temperatures[:8]
