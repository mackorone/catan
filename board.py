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
        return str(self.board)

    @staticmethod
    def height(size):
        return size * 2 - 1

    @staticmethod
    def row_width(size, row):
        return Board.height(size) - abs(row - size + 1)

    @staticmethod
    def blank(size):
        return [
            [None] * Board.row_width(size, row)
            for row in range(Board.height(size))
        ]
