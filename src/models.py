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

    def __init__(self, api_response=None, weather_info=None):
        """Constructor. Deserialize the JSON text and parse the parameters

        The Weather object may be created either independently or as a part of a Forecast object. In the second case,
        the API response will have already been deserialized, and the input will be a Python dict.

        Arguments:
        api_response -- the JSON response returned after calling OpenWeatherMap API
        weather_info -- dict that contains the api_response after deserializing the JSON
        """

        if weather_info is None and api_response is None:
            raise ValueError

        elif api_response is not None:
            # Deserializing the JSON text
            weather_info = json.loads(api_response)

        # Key to obtain the weather section of the JSON response
        weather_key = 'weather'
        weather_section = weather_info[weather_key][0]

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


