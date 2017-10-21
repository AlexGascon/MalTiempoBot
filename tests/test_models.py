import unittest
import json

from src.models import Weather


class TestWeather(unittest.TestCase):
    def setUp(self):
        self.json_api_response = open("./fixtures/weather.json").read()
        self.dict_api_response = json.loads(self.json_api_response)

    def test_json_constructor(self):
        test_weather = Weather(api_response=self.json_api_response)

        assert test_weather.id == 300
        assert test_weather.main == 'Drizzle'
        assert test_weather.description == 'light intensity drizzle'
        assert test_weather.icon == '09d'

    def test_dict_constructor(self):
        test_weather = Weather(weather_info=self.dict_api_response)

        assert test_weather.id == 300
        assert test_weather.main == 'Drizzle'
        assert test_weather.description == 'light intensity drizzle'
        assert test_weather.icon == '09d'


if __name__ == '__main__':
    unittest.__main__() 