from board import Board
from color import Color
from coordinate import Coordinate
from dice import Dice
from player import Player
from view import View


def main():
    board = Board(
        height=3,
        width=3,
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
    #print(Dice.possibilities())
    

if __name__ == '__main__':
    main()
