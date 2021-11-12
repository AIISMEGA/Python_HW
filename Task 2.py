from abc import ABC, abstractmethod

class Clothers(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return self.calculate + other.calculate

class Coat(Clothers):

    @property
    def calculate(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothers):
    @property
    def calculate(self):
        return (2 * self.param + 0.3) / 100

coat = Coat(78)
costume = Costume(274)
print(coat + costume)