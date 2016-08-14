from color import Color
from enum import Enum


class Resource(Enum):

    BRICK  = ('+', Color.RED)
    LUMBER = ('=', Color.BROWN)
    ORE    = ('^', Color.GRAY)
    SHEEP  = ('~', Color.GREEN)
    WHEAT  = ('|', Color.YELLOW)
    DESERT = (' ', None)

    def __str__(self):
        return self.name.lower()

    @property
    def char(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]
