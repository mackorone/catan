from board import Board
from tile import Tile
from resource import Resource


def main():
    # t = Tile(Resource.DESERT, None)
    # print(t.grid())
    b = Board(
        height=5,
        width=5,
    )
    print(b)

if __name__ == '__main__':
    main()
