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
        return str(Tile(Resource.ORE, 2))

    @staticmethod
    def row_width(size, row):
        return size * 2 - 1 - abs(row - size + 1)

    @staticmethod
    def blank(size):
        return [
            [Tile(Resource.SHEEP, 8)] * Board.row_width(size, row)
            for row in range(size * 2 - 1)
        ]
