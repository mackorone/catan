from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty,
)


class Path(metaclass=ABCMeta):

    def __init__(self, player):
        self.__player = player

    @property
    def player(self):
        return self.__player

    @abstractproperty
    def permanent(self):
        pass


class Road(Path):

    @property
    def permanent(self):
        return True
