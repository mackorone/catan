from pieces import (
    HEXAGONS,
    NUMBERS,
)
from random import shuffle
from resource import Resource
from tile import Tile


class Board(object):

    def __init__(self, height, width):
        Board._assert_valid_size(height, width)
        self.__height = height
        self.__width = width
        self._board = Board._generate(height, width)

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @staticmethod
    def _assert_valid_size(height, width):
        assert 1 <= height
        assert 1 <= width
        assert width % 2 == 1
        assert width < height * 2

    @staticmethod
    def _generate(height, width):

        # TODO: MACK - don't hardcode these
        hexagons = [
            res
            for res, count in HEXAGONS.items()
            for i in range(count)
        ]
        numbers = [
            num
            for num, count in NUMBERS.items()
            for i in range(count)
        ]
        shuffle(hexagons)
        shuffle(numbers)

        res_index = 0
        num_index = 0
        board = []
        for i in range(height):
            row = []
            for j in range(Board._row_size(height, width, i)):
                resource = hexagons[res_index]
                res_index += 1
                if resource == Resource.DESERT:
                    number = None
                else:
                    number = numbers[num_index]
                    num_index += 1      
                row.append(Tile(resource, number))
            board.append(row)
        return board

    @staticmethod
    def _row_size(height, width, row_number):
        Board._assert_valid_size(height, width)
        assert 0 <= row_number < height
        effective_row_number = (
            row_number
            if row_number <= (height + 1) // 2 - 1
            else height - 1 - row_number
        )
        return min(
            min(width, height),
            (width // 2 + 1) + effective_row_number,
        )

# TODO: Describe the sideways row/col
'''
                   + -- + 
                  /      \ 
            + -- +   00   + -- +
           /      \      /      \ 
     + -- +   10   + -- +   01   + -- +
    /      \      /      \      /      \
   +   20   + -- +   11   + -- +   02   +
    \      /      \      /      \      /
     + -- +   21   + -- +   12   + -- +
    /      \      /      \      /      \
   +   30   + -- +   22   + -- +   13   +
    \      /      \      /      \      /
     + -- +   31   + -- +   23   + -- +
    /      \      /      \      /      \
   +   40   + -- +   32   + -- +   24   +
  / \      /      \      /      \      /
 2=--+ -- +   41   + -- +   33   + -- +
           \      /      \      /
            + -- +   42   + -- +
                  \      / \
                   + -- +--2:
                    \  /
                     3?
'''
