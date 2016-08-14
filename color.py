from enum import Enum


class Color(Enum):

    BLUE   = 0
    BROWN  = 1
    GRAY   = 2
    GREEN  = 3
    ORANGE = 4
    RED    = 5
    WHITE  = 6
    YELLOW = 7

    def __str__(self):
        return self.name.lower()
