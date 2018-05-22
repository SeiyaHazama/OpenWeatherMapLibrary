"""
This library is can get weather from OpenWeatherMap.org.
To use this library, API key is needed in addition to this library.

OpenWeatherMap: https://openweathermap.org/
"""

___author___ = "Seiya Hazama"
___version___ = "1.0"
__date__ = "22 May 2018"

import urllib.request
import json
import datetime

class OpenWeatherMapLibrary:

    request_key = ""
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"

    def __init__(self, key):
        """
        Constructor.
        Set the parameter(API key) in request_key.

        @param key API key
        """
        self.request_key = key

    def getWeatherInfo(self, city):
        """
        Get weather information from OpenWeatherMap.
        Data format is JSON.

        @param city City name

        City name: Please search nearest city from OpenWeatherMap.
        """
        url = self.api.format(city=city, key=self.request_key)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        return data

    def getWeather(self, data):
        """
        Convert JSON to weather.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return String
        """
        return data["weather"][0]["main"]

    def getDetailedWeather(self, data):
        """
        Convert JSON to detail weather.
        This function is can get weather more than getWeather function.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return String
        """
        return data["weather"][0]["description"]

    def getTemperature(self, data):
        """
        Convert JSON to temperature.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return int
        """
        return data["main"]["temp"]

    def getWindSpeed(self, data):
        """
        Convert JSON to wind speed.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return float
        """
        return data["wind"]["speed"]

    def getSunriseTime(self, data):
        """
        Convert JSON to sunrise time.
        This function is return the converted local time from unix time.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return datetime
        """
        return self.toLocalTime(data["sys"]["sunrise"])

    def getSunsetTime(self, data):
        """
        Convert JSON to sunset time.
        This function is return the converted local time from unix time.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return datetime
        """
        return self.toLocalTime(data["sys"]["sunset"])

    def getCityName(self, data):
        """
        Convert JSON to city name.
        This function is return the city name of observation point.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return String
        """
        return data["name"]

    def getLocation(self, data):
        """
        Convert JSON to location information.
        This function is return the location information of observation point.
        JSON is can get from getWeatherInfo function.

        @param data JSON
        @return list[Longitude, Latitude]
        """
        location = []
        location.append(data["coord"]["lon"])
        location.append(data["coord"]["lat"])
        return location

    def toLocalTime(self, unixtime):
        """
        Convert UnixTime to LocalTime.

        @param unixtime UnixTime
        @return datetime
        """
        return datetime.datetime.fromtimestamp(unixtime)