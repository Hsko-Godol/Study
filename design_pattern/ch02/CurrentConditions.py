from DisplayElement import DisplayElement
from Observer import Observer
from Subject import Subject

class CurrentConditions(Observer, DisplayElement):
    def __init__(self, weatherData:Subject):
        self.temp = float
        self.humidity = float

        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp, humidity, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("This is the current conditions of the weather")
        print("Temperature :", self.temp, "C degrees")
        print("Humidity :", self.humidity, "%")

