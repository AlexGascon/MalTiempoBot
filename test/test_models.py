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

    def test_weather_is_bad_returns_false_when_weather_is_good(self):
        """Testing that the method Weather.is_bad() returns True when the weather condition is a good one"""
        test_weather = Weather(weather_info=self.dict_api_response)

        test_weather.id = 800
        self.assertFalse(test_weather.is_bad())
        test_weather.id = 801
        self.assertFalse(test_weather.is_bad())
        test_weather.id = 802
        self.assertFalse(test_weather.is_bad())
        test_weather.id = 803
        self.assertFalse(test_weather.is_bad())
        test_weather.id = 804
        self.assertFalse(test_weather.is_bad())
        test_weather.id = 951
        self.assertFalse(test_weather.is_bad())

    def test_weather_is_bad_returns_true_when_weather_is_bad(self):
        """Testing that the method Weather.is_bad() returns True when the weather condition is a good one"""
        test_weather = Weather(weather_info=self.dict_api_response)

        test_weather.id = 300
        self.assertTrue(test_weather.is_bad())
        test_weather.id = 473
        self.assertTrue(test_weather.is_bad())
        test_weather.id = 2432
        self.assertTrue(test_weather.is_bad())


if __name__ == '__main__':
    unittest.__main__()
