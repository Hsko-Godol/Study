import abc

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
