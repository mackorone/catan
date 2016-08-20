from board import Board
from color import Color
from player import Player
from view import View


def main():
    board = Board(
        height=5,
        width=5,
    )
    one = Player(
        name='one',
        color=Color.RED,
    )
    board.build_settlement(
        row=0,
        column=0,
        corner=1,
        player=one,
    )
    print(View(board))
    

if __name__ == '__main__':
    main()
