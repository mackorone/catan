from graphics import TILE_LINES
from resource import Resource
from tile import Tile


class InvalidBoardSizeError(Exception):
    pass


class Board(object):

    def __init__(self, size):
        if size < 1:
            raise InvalidBoardSizeError
        # TODO: Needed?
        self.size = size
        self.board = Board.blank(size)

    def __str__(self):
        # return '\n'.join([
        #     str(Tile(Resource.BRICK, 2)),
        #     '\n'.join(str(Tile(Resource.DESERT, 2)).split('\n')[1:]),
        #     '\n'.join(str(Tile(Resource.LUMBER, 3)).split('\n')[1:]),
        #     '\n'.join(str(Tile(Resource.ORE,12)).split('\n')[1:]),
        #     '\n'.join(str(Tile(Resource.SHEEP, 9)).split('\n')[1:]),
        #     '\n'.join(str(Tile(Resource.WHEAT, 8)).split('\n')[1:]),
        # ])
        
        # TODO: MACK - put all hardcoded logic in one place

        tile_height = len(TILE_LINES)
        tile_narrow = len(TILE_LINES[0].strip())
        tile_wide = len(TILE_LINES[len(TILE_LINES) // 2].strip())

        total_height = (tile_height - 1) * len(self.board) + 1
        total_width = (
            (self.size    ) * (tile_wide   - 1) +
            (self.size - 1) * (tile_narrow - 1) + 1
        )
        chars = [
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

                for tile_i, tile_line in enumerate(tile.chars()):
                    for tile_j, char in enumerate(tile_line):
                        if char == ' ':
                            continue
                        try:
                            chars[spaces_from_top + tile_i][spaces_from_left + tile_j] = char
                        except:
                            pass
                    
        return '\n'.join([''.join(line) for line in chars])
        

    # TODO: MACK - kill this
    @staticmethod
    def row_width(size, row_number):
        return size * 2 - 1 - abs(row_number - size + 1)

    @staticmethod
    def blank(size):
        return [
            [Tile(Resource.SHEEP, 8)] * Board.row_width(size, row_number)
            for row_number in range(size * 2 - 1)
        ]

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
    \      /      \      /      \      /
     + -- +   41   + -- +   33   + -- +
           \      /      \      /
            + -- +   42   + -- +
                  \      /
                   + -- + 
'''
