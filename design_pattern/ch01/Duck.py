import abc

from QuackBehavior import QuackBehavior
from FlyBehavior import FlyBehavior

class Duck(metaclass=abc.ABCMeta):
    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("SWIM~")

    @abc.abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def setQuackBehavior(self, qb:QuackBehavior):
        self.quackBehavior:QuackBehavior = qb

    def setFlyBehavior(self, fb:FlyBehavior):
        self.flyBehavior:FlyBehavior = fb
