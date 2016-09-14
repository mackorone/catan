from board import Board
from color import Color
from coordinate import (
    Coordinate,
    get_all_neighbors,
    get_valid_neighbors,
)
from dice import Dice
from player import Player
from pprint import pprint
from size import Size
from view import View
from intersection import (
    Intersection,
    get_intersection_group,
)


def main():

    # Create the board
    size = Size(
        height=5,
        width=5,
    )
    board = Board(
        size=size,
    )

    # Create the players
    one = Player(
        name='one',
        color=Color.RED,
    )

    # Build a settlement
    intersection = Intersection(
        row=2,
        column=2,
        corner=3,
    )
    board.build_settlement(
        intersection=intersection,
        player=one,
    )

    print(View(board))
    

if __name__ == '__main__':
    main()
