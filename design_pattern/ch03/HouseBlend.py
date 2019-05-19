from Beverage import Beverage

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "하우스 블렌드 커피"

    def cost(self):
        return .89

