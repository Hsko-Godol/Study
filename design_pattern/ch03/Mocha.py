from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Mocha(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 모카"

    def cost(self):
        cost = self.beverage.cost()

        if self.getSize() == "Tall":
            cost += .15
        elif self.getSize() == "Grande":
            cost += .20
        elif self.getSize() == "Venti":
            cost += .25

        return cost

