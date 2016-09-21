from color import Color


class Player(object):

    _NEXT_NUMBER = 1

    def __init__(self: 'Player', name: str, color: 'Color'):
        self.__number = Player._get_next_number()
        self.__name = name
        self.__color = color
        self.__pieces = {
            # TODO        
        }
        self.__resources = {
            # TODO        
        }
        self.__development_cards = {
            # TODO        
        }

    def __str__(self: 'Player'):
        return 'Player(number={}, name="{}")'.format(
            self.__number,
            self.__name,
        )

    @classmethod
    def _get_next_number(cls):
        number = cls._NEXT_NUMBER
        cls._NEXT_NUMBER += 1
        return number

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color
