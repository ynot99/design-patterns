# Observer

Task: Implement a simple weather monitoring system using the Observer design pattern.

Description: Your task is to create a weather monitoring system that allows multiple weather displays to receive updates whenever the weather changes. The system should consist of three classes: WeatherData, Display, and WeatherObserver.

The WeatherData class should have the following responsibilities:

- Store the current temperature, humidity, and pressure values.
- Provide methods to update the weather data and notify all registered observers.
- Maintain a list of registered observers.

The Display class should have the following responsibilities:

- Display the current weather data (temperature, humidity, and pressure).
- Be able to register and unregister with the WeatherData class as an observer.
- Update its display when notified by the WeatherData class.

The WeatherObserver interface should define the following methods:

- update(float temperature, float humidity, float pressure): This method will be called by the WeatherData class to notify observers of changes in weather data.

Instructions:

1. Implement the WeatherObserver interface with an update method.
2. Create the WeatherData class with appropriate methods and data members to store weather data and manage observers.
3. Implement the Display class, which should be able to register and unregister with the WeatherData class and update its display when notified.
4. Create multiple Display objects to represent different weather displays that will observe the WeatherData class.
5. Test your implementation by updating the weather data in the WeatherData class and verifying that all registered displays receive updates accordingly.

This task will help you practice the Observer design pattern, which allows objects to observe and automatically update when the state of another object changes.
@ChatGPT
