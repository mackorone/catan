from enum import Enum


class Color(Enum):

    BLUE = 0
    RED = 1
    WHITE = 2
    ORANGE = 3

    def __str__(self):
        return self.name.lower()
