from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Mocha(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 모카"

    def cost(self):
        return .20 + self.beverage.cost()

