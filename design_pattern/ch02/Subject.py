import abc

from Observer import Observer

class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def registerObserver(self, o:Observer):
        pass

    @abc.abstractmethod
    def removeObserver(self, o:Observer):
        pass

    @abc.abstractmethod
    def notifyObservers(self):
        pass
