import abc

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temp, humidity, wind_speed):
        pass

