import abc

class DisplayElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        pass

