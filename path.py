from abc import (
    ABCMeta,
    abstractmethod,
)


class Path(metaclass=ABCMeta):

    def __init__(self, team, edge):
        self.__team = team
        self.__edge = edge

    @property
    def team(self):
        return self.__team

    @property
    def edge(self):
        return self.__edge

    @abstractproperty
    def permanent(self):
        pass
