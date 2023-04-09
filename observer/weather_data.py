from display import Display
from weather_observer import WeatherObserver


class WeatherData:
    def __init__(self) -> None:
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0
        self.observers: list[WeatherObserver] = []

    def register_observer(self, observer: WeatherObserver) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: WeatherObserver) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
