from color import Color


class Player(object):

    def __init__(self, name, color):
        assert isinstance(color, Color)
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color
