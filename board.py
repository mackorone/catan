from graphics import (
    TILE_GRID,
    grid_to_str,
)
from pieces import (
    HEXAGONS,
    NUMBERS,
)
from random import shuffle
from resource import Resource
from tile import Tile


class Board(object):

    def __init__(self, height, width):
        for x in [height, width]:
            assert 1 <= x
            assert x % 2 == 1
        self.__height = height
        self.__width = width
        self.size = 3 # TODO
        self.board = Board.generate(self.size)

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def __str__(self, fancy=True):

        # TODO: MACK- return a grid, convert to string
        
        # TODO: MACK - put all hardcoded logic in one place

        tile_height = len(TILE_GRID)
        tile_narrow = len(''.join(TILE_GRID[0]).strip())
        tile_wide = len(''.join(TILE_GRID[len(TILE_GRID) // 2]).strip())

        total_height = (tile_height - 1) * len(self.board) + 1
        total_width = (
            (self.size    ) * (tile_wide   - 1) +
            (self.size - 1) * (tile_narrow - 1) + 1
        )
        grid = [
            [' ' for i in range(total_width)]
            for j in range(total_height)
        ]

        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):

                # TODO: MACK - Clean this logic up
                if i < self.size:
                    spaces_from_top = (i + j) * (tile_height // 2)
                else:
                    spaces_from_top = (
                        ((self.size - 1 + j) * (tile_height // 2)) +
                        ((i - (self.size - 1)) * (tile_height - 1))
                    )
                if i < self.size:
                    spaces_from_left = (
                        ((self.size * 2 - 1) - len(row) + j) *
                        ((tile_wide + tile_narrow) // 2 - 1)
                    )
                else:
                    spaces_from_left = (
                        j * ((tile_wide + tile_narrow) // 2 - 1)
                    )

                for tile_i, tile_line in enumerate(tile.grid(fancy=fancy)):
                    for tile_j, char in enumerate(tile_line):
                        if char != ' ':
                            grid[spaces_from_top + tile_i][spaces_from_left + tile_j] = char
                    
        return grid_to_str(grid)
        

    # TODO: MACK - kill this
    @staticmethod
    def row_width(size, row_number):
        return size * 2 - 1 - abs(row_number - size + 1)

    @staticmethod
    def generate(size):

        hexagons = [
            res
            for res, count in HEXAGONS.items()
            for i in range(count)
        ]
        shuffle(hexagons)

        numbers = [
            num
            for num, count in NUMBERS.items()
            for i in range(count)
        ]
        shuffle(numbers)

        res_index = 0
        num_index = 0
        board = []
        for i in range(size * 2 - 1):
            row = []
            for j in range(Board.row_width(size, i)):
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
