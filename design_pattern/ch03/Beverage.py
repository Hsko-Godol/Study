import abc

class Beverage(metaclass=abc.ABCMeta):
    def __init__(self):
        self.description = "제목없음"

    def getDescription(self):
        return self.description

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    @abc.abstractmethod
    def cost(self):
        pass

