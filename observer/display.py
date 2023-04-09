from weather_observer import WeatherObserver


class Display(WeatherObserver):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def update(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        print("Display {} updated with new weather data:".format(self.name))
        print(
            "Temperature: {}C, Humidity: {}%, Pressure: {}Pa".format(
                temperature, humidity, pressure
            )
        )
