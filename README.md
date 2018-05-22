# OpenWeatherMapLibrary

## Overview

This library is can easy get weather information from OpenWeatherMap.org.

## About OpenWeatherMap

OpenWeatherMap is online service to get weather for developer. OpenWeatherMap is can get format for JSON, XML, HTML. This library is use JSON.

To use this library, API key is needed in addition to this library.

[OpenWeatherMap](https://openweathermap.org/)

## Installation

1. Clone this repository.
    ```shellscript
    $ git clone git@github.com:SeiyaHazama/OpenWeatherMapLibrary.git
    ```
2. Placement this library to project folder. Please
3. Import this library. 
    * Example(Pattern: project file is in the same directory)
    ```python3
    from OpenWeatherMapLibrary import OpenWeatherMapLibrary
    ```
4. You can use this library!

## Reference

Please see OpenWeatherMapLibrary.html.

## Example

This Sample is get weather in Toyota,JP. this program is as same as Example.py.

### Directory

.  
├── Example.py  
├── OpenWeatherMapLibrary.html  
└── OpenWeatherMapLibrary.py  

### Code

```python3
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
```

Thank you watch this repository!!
