from board import Board
from color import Color
from coordinate import Coordinate
from dice import Dice
from player import Player
from size import Size
from view import View


def main():
    board = Board(
        size=Size(
            height=5,
            width=5,
        ),
    )
    one = Player(
        name='one',
        color=Color.RED,
    )
    # board.build_settlement(
    #     row=2,
    #     column=2,
    #     corner=3,
    #     player=one,
    # )
    print(View(board))
    

if __name__ == '__main__':
    main()
