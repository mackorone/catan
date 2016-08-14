from resource import Resource
from tile import Tile


class InvalidBoardSizeError(Exception):
    pass


class Board(object):

    def __init__(self, size):
        if size < 1:
            raise InvalidBoardSizeError
        self.size = size
        self.board = Board.blank(size)

    def __str__(self):
        return '\n'.join([
            str(Tile(Resource.BRICK, 2)),
            '\n'.join(str(Tile(Resource.DESERT, 2)).split('\n')[1:]),
            '\n'.join(str(Tile(Resource.LUMBER, 3)).split('\n')[1:]),
            '\n'.join(str(Tile(Resource.ORE,12)).split('\n')[1:]),
            '\n'.join(str(Tile(Resource.SHEEP, 9)).split('\n')[1:]),
            '\n'.join(str(Tile(Resource.WHEAT, 8)).split('\n')[1:]),
        ])
        # tile_lines = s tr(Tile(Resource.SHEEP, 8)).split('\n')
        # print(tile_lin es)
        # narrow = len(t ile_lines[0])
        # wide = len(til e_lines[len(tile_lines) // 2])
        # lines = []     
        # print(narrow)  
        # print(wide)   ]
        # # TODO: MACK - overwrite only if not space
        # return 'foo'
        

    # TODO: MACK - kill this
    @staticmethod
    def row_width(size, row):
        return size * 2 - 1 - abs(row - size + 1)

    @staticmethod
    def blank(size):
        return [
            [Tile(Resource.SHEEP, 8)] * Board.row_width(size, row)
            for row in range(size * 2 - 1)
        ]

# TODO: Describe the sideways row/col
'''
         0 -- 0 
        / rrrr \ 
  0 -- 0 r ## r 0 -- 0
 / rrrr \ rrrr / rrrr \ 
0 r ## r 0 -- 0 r ## r 0
 \ rrrr / rrrr \ rrrr /
  0 -- 0 r ## r 0 -- 0
 / rrrr \ rrrr / rrrr \ 
0 r ## r 0 -- 0 r ## r 0
 \ rrrr / rrrr \ rrrr /
  0 -- 0 r ## r 0 -- 0
        \ rrrr /
         0 -- 0 
'''
