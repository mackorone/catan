from pieces import (
    HEXAGONS,
    NUMBERS,
)
from random import shuffle
from resource import Resource
from tile import Tile


class Board(object):
    """ Model of the game board

    Rows go from the upper left to the lower right, i.e.:

             + -- + 
            /      \ 
      + -- +   00   + -- +
     /      \      /      \ 
    +   10   + -- +   01   +     
     \      /      \      /       
      + -- +   11   + -- +         
     /      \      /      \       
    +   21   + -- +   12   +     
     \      /      \      /       
      + -- +   22   + -- +         
            \      /              
             + -- +              
    """
    def __init__(self, height, width):
        Board._assert_valid_size(height, width)
        self.__height = height
        self.__width = width
        self.__board = Board._generate(height, width)

    def __iter__(self):
        return iter(self.__board)

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

        # TODO: MACK - hardcoded for 5 right now
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
