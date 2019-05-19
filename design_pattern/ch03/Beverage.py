import abc

class Beverage(metaclass=abc.ABCMeta):
    def __init__(self):
        self.description = "제목없음"

    def getDescription(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass

