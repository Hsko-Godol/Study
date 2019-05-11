from Duck import Duck

from QuackBehavior import QuackBehavior
from Quack import Quack

from FlyBehavior import FlyBehavior
from FlyNoWay import FlyNoWay

class RubberDuck(Duck):
    def __init__(self):
        self.quackBehavior:QuackBehavior = Quack()
        self.flyBehavior:FlyBehavior = FlyNoWay()

    def display(self):
        print("I'm a rubber duck")

if __name__ == '__main__':
    rd = RubberDuck()

    rd.performQuack()
    rd.swim()
    rd.display()
    rd.performFly()
