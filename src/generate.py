from coordinate import (
    get_valid_coordinates,
    get_valid_neighbors,
)
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


    # Get red number coordinates
    coordinates = list(get_valid_coordinates(size))
    first_four_touching = False
    while first_four_touching:
        first_four_touching = False
        shuffle(coordinates)
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                if coordinates[i] in get_valid_neighbors(size, coordinates[j]):
                    first_four_touching = True

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
