from abc import (
    ABCMeta,
    abstractproperty,
)


class Building(metaclass=ABCMeta):

    def __init__(self, team, location):
        self.__team = team
        self.__location = location

    @property
    def team(self):
        return self.__team

    @property
    def location(self):
        return self.__location

    @abstractproperty
    def multiplier(self):
        pass
