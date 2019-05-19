from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Whip(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 휘핑 크림"

    def cost(self):
        return .10 + self.beverage.cost()

