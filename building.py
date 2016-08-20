from abc import (
    ABCMeta,
    abstractproperty,
)


class Building(metaclass=ABCMeta):

    def __init__(self, player):
        self.__player = player

    @property
    def player(self):
        return self.__player

    @abstractproperty
    def multiplier(self):
        pass
