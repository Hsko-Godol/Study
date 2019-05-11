from Duck import Duck

from QuackBehavior import QuackBehavior
from Quack import Quack

from FlyBehavior import FlyBehavior
from FlyNoWay import FlyNoWay

class ModelDuck(Duck):
    def __init__(self):
        self.quackBehavior:QuackBehavior = Quack()
        self.flyBehavior:FlyBehavior = FlyNoWay()

    def display(self):
        print("I'm a model duck!")

if __name__ == '__main__':
    md = ModelDuck()

    md.performQuack()
    md.swim()
    md.display()
    md.performFly()
