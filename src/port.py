from color import Color
from enum import Enum


class Resource(Enum):

    BRICK  = ('=', Color.RED)
    LUMBER = ('|', Color.GREEN)
    ORE    = ('^', Color.BLUE)
    SHEEP  = (':', Color.WHITE)
    WHEAT  = ('~', Color.YELLOW)
    DESERT = (' ', Color.DEFAULT)
    WILD   = ('?', Color.DEFAULT)

    @property
    def char(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]
