from Beverage import Beverage

class Decaf(Beverage):
    def __init__(self):
        self.description = "디카페인"

    def cost(self):
        return 1.05

