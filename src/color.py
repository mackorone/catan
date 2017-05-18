from config import Config
from enum import Enum


class Color(Enum):

    DEFAULT = 0
    RED     = 31
    GREEN   = 32
    YELLOW  = 33
    BLUE    = 34
    WHITE   = 37
    GRAY    = 90

    def apply(self, string, light=False):
        if Config.NO_COLOR:
            return string
        template = '\033[{}{{}}m'.format('1;' if light else '')
        return '{}{}{}'.format(
            template.format(self.value),
            string,
            template.format(Color.DEFAULT.value),
        )
