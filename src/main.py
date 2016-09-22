from board import Board
from building import (
    City,
    Settlement,
)
from color import Color
from player import Player
from size import Size
from view import View
from intersection import Intersection


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
    two = Player(
        name='two',
        color=Color.BLUE,
    )

    # Build two settlements and a city
    intersection = Intersection(
        row=2,
        column=2,
        corner=3,
    )
    board.build_building(
        intersection=intersection,
        building=one.take_piece(Settlement),
    )
    board.build_building(
        intersection=intersection,
        building=one.take_piece(City),
    )
    board.build_building(
        intersection=Intersection(
            row=2,
            column=1,
            corner=1,
        ),
        building=two.take_piece(Settlement),
    )

    # Print the board
    print(View(board))


if __name__ == '__main__':
    main()
