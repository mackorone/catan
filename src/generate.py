from coordinate import get_valid_coordinates
from pieces import (
    HEXAGONS,
    NUMBERS,
)
from random import shuffle
from resource import Resource
from size import Size
from tile import Tile


def generate_board(size):
    """ Returns a map from Coordinates to Tiles
    """
    # TODO: Hardcoded for size 5 right now
    # TODO: Ensure that two red numbers don't neighbor each other
    hexagons = [
        res
        for res, count in HEXAGONS.items()
        for i in range(count)
    ]
    numbers = [
        num
        for num, count in NUMBERS.items()
        for i in range(count)
    ]
    shuffle(hexagons)
    shuffle(numbers)

    res_index = 0
    num_index = 0
    board = dict()
    for coordinate in get_valid_coordinates(size):
        resource = hexagons[res_index]
        res_index += 1
        if resource == Resource.DESERT:
            number = None
        else:
            number = numbers[num_index]
            num_index += 1      
        board[coordinate] = Tile(resource, number)
    return board
