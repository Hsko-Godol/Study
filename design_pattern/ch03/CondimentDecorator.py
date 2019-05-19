import abc
from Beverage import Beverage

class CondimentDecorator(Beverage):
    @abc.abstractmethod
    def getDescription(self):
        pass
