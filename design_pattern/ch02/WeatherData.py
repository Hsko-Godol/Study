from Subject import Subject
from Observer import Observer

class WeatherData(Subject):
    def __init__(self):
        self.observers = []

    def registerObserver(self, o:Observer):
        self.observers.append(o)

    def removeObserver(self, o:Observer):
        i = self.observers.index(o)
        if i >= 0:
            del self.observers[i]

    def notifyObservers(self):
        for o in self.observers:
            o.update(self.temp, self.humidity, self.wind_speed)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp, humidity, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.measurementsChanged()

if __name__ == '__main__':
    wd = WeatherData()

    print(wd.temp)
    print(wd.humidity)
    print(wd.wind_speed)

    wd.setMeasurements()

    print(wd.temp)
    print(wd.humidity)
    print(wd.wind_speed)
