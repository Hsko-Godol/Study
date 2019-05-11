from Duck import Duck

from QuackBehavior import QuackBehavior
from Squeak import Squeak

from FlyBehavior import FlyBehavior
from FlyWithWings import FlyWithWings

class RedheadDuck(Duck):
    def __init__(self):
        self.quackBehavior:QuackBehavior = Squeak()
        self.flyBehavior:FlyBehavior = FlyWithWings()

    def display(self):
        print("I'm a red head duck!")

if __name__ == '__main__':
    rd = RedheadDuck()

    rd.performQuack()
    rd.swim()
    rd.display()
    rd.performFly()
