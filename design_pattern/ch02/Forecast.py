from DisplayElement import DisplayElement
from Observer import Observer
from Subject import Subject

class Forecast(Observer, DisplayElement):
    def __init__(self, weatherData:Subject):
        self.temp = float
        self.humidity = float
        self.wind_speed = float

        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp, humidity, wind_speed):
        self.temp = temp + 1.0
        self.humidity = humidity + 5.0
        self.wind_speed = wind_speed + 0.5

        self.display()

    def display(self):
        print("This is the forecast of the weather")
        print("Temperature :", self.temp, "C")
        print("Humidity :", self.humidity, "%")
        print("Wind Speed :", self.wind_speed, "m/s")

