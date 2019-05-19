from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Soy(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 두유"

    def cost(self):
        return .15 + self.beverage.cost()

