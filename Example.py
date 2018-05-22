# Import OpenWeatherMapLibrary
from OpenWeatherMapLibrary import OpenWeatherMapLibrary

# API key
key = "(API key)"

# Instantiation of OpenWeatherMap Library
owm = OpenWeatherMapLibrary(key)

# Get weather information from OpenWeatherMap.org
# City name list: http://openweathermap.org/help/city_list.txt
data = owm.getWeatherInfo("Toyota,JP")

# Convert JSON to Weather(String)
weather = owm.getWeather(data)

# Print weather
print(weather)