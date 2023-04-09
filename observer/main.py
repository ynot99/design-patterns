from display import Display
from weather_data import WeatherData


weather_data = WeatherData()
weather_data.register_observer(Display("firstobs"))
weather_data.set_measurements(20.3, 50.0, 1000.0)

weather_data.register_observer(Display("secondobs"))
weather_data.register_observer(Display("thirdobs"))
weather_data.set_measurements(17.7, 60.0, 1010.0)
