from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class SteamMilk(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 스팀 밀크"

    def cost(self):
        cost = self.beverage.cost()

        if self.getSize() == "Tall":
            cost += .05
        elif self.getSize() == "Grande":
            cost += .10
        elif self.getSize() == "Venti":
            cost += .15

        return cost

