from board import Board
from board_graphic import BoardGraphic
from resource import Resource
from tile import Tile
from tile_graphic import TileGraphic


def main():
    # t = Tile(Resource.BRICK, 5)
    # print(TileGraphic(t))
    board = Board(
        height=3,
        width=5,
    )
    board_graphic = BoardGraphic(
        board=board,
    )
    print(board_graphic)

if __name__ == '__main__':
    main()
