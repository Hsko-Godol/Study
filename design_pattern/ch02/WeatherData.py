from CurrentConditions import CurrentConditions
from Statistics import Statistics
from Forecast import Forecast

class WeatherData:
    def __init__(self):
        self.currentConditionsDisplay = CurrentConditions()
        self.statisticsDisplay = Statistics()
        self.forecastDisplay = Forecast()

        self.temp = 22.0
        self.humidity = 4.0
        self.wind_speed = 5.0

    def getTemperature(self):
        self.temp += 1
        if self.temp == 40.0:
            self.temp = 18.0
        return self.temp

    def getHumidity(self):
        self.humidity += 5
        if self.humidity == 100.0:
            self.humidity = 0.0
        return self.humidity

    def getWindSpeed(self):
        self.wind_speed += 0.5
        if self.wind_speed == 10.0:
            self.wind_speed = 1.0
        return self.wind_speed

    def measurementsChanged(self):
        temp       = self.getTemperature()
        humidty    = self.getHumidity()
        wind_speed = self.getWindSpeed()

        self.currentConditionsDisplay.update(self.temp, self.humidity, self.wind_speed)
        self.statisticsDisplay.update(self.temp, self.humidity, self.wind_speed)
        self.forecastDisplay.update(self.temp, self.humidity, self.wind_speed)

if __name__ == '__main__':
    wd = WeatherData()

    print(wd.getTemperature())
    print(wd.getHumidity())
    print(wd.getWindSpeed())

    wd.measurementsChanged()
    wd.currentConditionsDisplay.display()
    wd.statisticsDisplay.display()
    wd.forecastDisplay.display()
