import unittest
import json

from src.models import Weather


class TestWeather(unittest.TestCase):
    """Testing the Weather model of the project"""

    def setUp(self):
        self.json_api_response = open("./fixtures/weather.json").read()
        self.dict_api_response = json.loads(self.json_api_response)

    def test_json_constructor(self):
        """Weather objects can be correctly created from OWM api response in JSON format"""

        test_weather = Weather(api_response=self.json_api_response)

        self.assertEqual(test_weather.id, 300)
        self.assertEqual(test_weather.main, 'Drizzle')
        self.assertEqual(test_weather.description, 'light intensity drizzle')
        self.assertEqual(test_weather.icon, '09d')

    def test_dict_constructor(self):
        """Weather objects can be correctly created from a dict containing OWM's API response"""

        test_weather = Weather(weather_info=self.dict_api_response)

        self.assertEqual(test_weather.id, 300)
        self.assertEqual(test_weather.main, 'Drizzle')
        self.assertEqual(test_weather.description, 'light intensity drizzle')
        self.assertEqual(test_weather.icon, '09d')


if __name__ == '__main__':
    unittest.__main__()