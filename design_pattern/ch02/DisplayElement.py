import abc

class DisplayElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        pass

    def update(self, temp, humidity, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
