from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v
        self.length = round(float(self.v) / 6.5 + 0.5)

    @property
    def fabric(self):
        return f'Расход ткани на пальто: {self.length} м'

    def __add__(self, other):
        return f'Общий расход: {self.length + other.length / 100} м'


class Costume(Clothes):
    def __init__(self, h):
        self.h = h
        self.length = round(float(self.h) * 2 + 0.3)

    @property
    def fabric(self):
        return f'Расход ткани на костюм: {self.length} cм'


coat = Coat(38)
print(coat.fabric)
costume = Costume(180)
print(costume.fabric)
print(coat + costume)
