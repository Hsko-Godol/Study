from DisplayElement import DisplayElement
from Observer import Observer
from Subject import Subject

class Statistics(Observer, DisplayElement):
    def __init__(self, weatherData:Subject):
        self.temp = float
        self.humidity = float
        self.wind_speed = float

        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp, humidity, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed

        self.display()

    def display(self):
        print("This is the statistics of the weather")

        print("Temperature")
        print("\t- MIN =", self.temp)
        print("\t- AVG =", self.temp)
        print("\t- MAX =", self.temp)

        print("Humidity")
        print("\t- MIN =", self.humidity)
        print("\t- AVG =", self.humidity)
        print("\t- MAX =", self.humidity)

        print("Wind Speed")
        print("\t- MIN =", self.wind_speed)
        print("\t- AVG =", self.wind_speed)
        print("\t- MAX =", self.wind_speed)
