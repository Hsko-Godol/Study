from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Soy(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", 두유"

    def cost(self):
        cost = self.beverage.cost()

        if self.getSize() == "Tall":
            cost += .10
        elif self.getSize() == "Grande":
            cost += .15
        elif self.getSize() == "Venti":
            cost += .20

        return cost

