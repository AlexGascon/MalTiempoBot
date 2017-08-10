import json

from constants import WEATHER_GROUP_GOOD_WEATHER


class Weather:
    """Weather information obtained when calling the OpenWeatherMap API

    Parameters:
        id -- unique identifier for the weather condition
        main -- group of weather parameters (Rain, Snow, Extreme etc.)
        description -- description of the weather condition
        icon -- weather condition ID (currently unused)
    """

    def __init__(self, api_response):
        """Constructor. Deserialize the JSON text and parse the parameters

        Arguments:
        api_response -- the response returned after calling OpenWeatherMap API
        """
        # Deserializing the JSON text
        json_text = json.loads(api_response)

        # Key to obtain the weather section of the JSON response
        weather_key = 'weather'
        weather_section = json_text[weather_key]

        # Assigning the parameters
        self.id = weather_section['id']
        self.main = weather_section['main']
        self.description = weather_section['description']
        self.icon = weather_section['icon']

    def is_bad(self):
        """Return a boolean indicating if the weather is bad (rain, snow...)"""
        return self.id not in WEATHER_GROUP_GOOD_WEATHER


class Forecast:
    """Collection of Weather objects

    Parameters:
        weathers -- Weather conditions included in the forecast
    """

    def __init__(self, api_response, days=None):
        """Constructor. Deserialize the JSON text and parse the parameters

        Arguments:
        api_response -- the response returned after calling OpenWeatherMap API
        days -- Integer representing the amount of days our Forecast will show. If None, we won't cut the API response.
        """

        self.weathers = []

        # Deserializing the JSON text
        json_text = json.loads(api_response)

        # Key to obtain the weather section of the JSON response
        weather_list = json_text['list']

        temp_weathers = []

        for weather_info in weather_list:
            temp_weathers.append(Weather(api_response=weather_info))

        # Limiting the amount of weathers in the Forecast if necessary
        if days is not None:
            self.weathers = temp_weathers[:days*8]
        else:
            self.weathers = temp_weathers

    def is_bad(self):
        """Return a boolean indicating if any of the weathers in the forecast is bad"""
        return any((weather.is_bad() for weather in self.weathers))


