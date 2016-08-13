from abc import (
    ABCMeta,
    abstractproperty,
)


class Building(metaclass=ABCMeta):

    def __init__(self, color, location):
        self.__color = color
        self.__location = location

    @property
    def color(self):
        return self.__color

    @property
    def location(self):
        return self.__location

    @abstractproperty
    def multiplier(self):
        pass
