from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class SteamMilk(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 스팀 밀크"

    def cost(self):
        return .1 + self.beverage.cost()

