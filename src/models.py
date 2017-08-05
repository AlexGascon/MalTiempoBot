import json

from constants import WEATHER_GROUP_GOOD_WEATHER


class Weather:
    """Represents the weather information obtained when calling the OpenWeatherMap API"""

    def __init__(self, api_response):
        """Constructor. Deserializes the JSON text and parses the parameters"""
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
        """Method that returns a boolean indicating if the weather is bad (rain, snow, thunderstorm...)"""
        return self.id not in WEATHER_GROUP_GOOD_WEATHER
    