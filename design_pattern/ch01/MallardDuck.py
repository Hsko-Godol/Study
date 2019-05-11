from Duck import Duck

from QuackBehavior import QuackBehavior
from Quack import Quack

from FlyBehavior import FlyBehavior
from FlyWithWings import FlyWithWings

class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior:QuackBehavior = Quack()
        self.flyBehavior:FlyBehavior = FlyWithWings()

    def display(self):
        print("I'm a mallard duck!")

if __name__ == '__main__':
    md = MallardDuck()

    md.performQuack()
    md.swim()
    md.display()
    md.performFly()
