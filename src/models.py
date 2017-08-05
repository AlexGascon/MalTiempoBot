import json


class Weather:
    """Represents the weather information obtained when calling the OpenWeatherMap API"""

    def __init__(self, api_response):

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