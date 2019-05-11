import abc

class Duck(metaclass=abc.ABCMeta):
    def quack(self):
        print("QUACK!")

    def swim(self):
        print("SWIM~")

    @abc.abstractmethod
    def display(self):
        pass
