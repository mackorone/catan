from building import (
    City,
    Settlement,
)
from color import Color
from error import NoSuchPieceError
from path import Road
from typing import Union


class Player(object):

    _NEXT_NUMBER = 1

    def __init__(self: 'Player', name: str, color: 'Color'):
        self.__number = Player._get_next_number()
        self.__name = name
        self.__color = color
        self.__pieces = set()
        self.__resources = set()
        self.__development_cards = set()

        # Add the initial pieces
        for cls, count in [
            (Settlement, 5),
            (City, 4),
            (Road, 15),
        ]:
            for i in range(count):
                self.__pieces.add(cls(self))

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

    def add_piece(self: 'Player', piece: Union[Settlement, City, Road]):
        """ Inserts a piece into the players set of pieces
        """
        self.__pieces.add(piece)

    def take_piece(self: 'Player', cls: type):
        """ Returns a piece (of a given type cls) from the players set of pieces
        """
        try:
            piece = next(x for x in self.__pieces if isinstance(x, cls))
            self.__pieces.remove(piece)
            return piece
        except StopIteration:
            raise NoSuchPieceError(
                '{} has no more {} pieces'.format(
                    str(self),
                    cls.__name__,
                )
            )
