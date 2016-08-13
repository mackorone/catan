from enum import Enum


class Resource(Enum):

    BRICK = 0
    LUMBER = 1
    ORE = 2
    SHEEP = 3
    WHEAT = 4

    def __str__(self):
        return self.name
