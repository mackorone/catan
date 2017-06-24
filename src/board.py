from coordinate import Coordinate
from orientation import Orientation
from random import shuffle
from resource import Resource
from size import Size
from tile import (
    Harbor,
    Terrain,
)
from view import View


def yield_next_resource():
    order = 3 * [
       Resource.LUMBER, 
       Resource.BRICK, 
       Resource.SHEEP,
       Resource.WHEAT,
       Resource.ORE,
    ] + [
       Resource.LUMBER, 
       Resource.SHEEP,
       Resource.WHEAT,
       Resource.DESERT,
    ]
    i = 0
    while True:
        yield order[i % len(order)]
        i += 1


def yield_next_number():
    order = [
        6,  8,
        5,  9,
        4, 10,
        3, 11,
        2, 12,
        6,  8,
        5,  9,
        4, 10,
        3, 11,
    ]
    i = 0
    while True:
        yield order[i % len(order)]
        i += 1


class Board(object):

    def __init__(self, height, width):
        self.size = Size(height, width)
        self.shuffle()

    def __str__(self):
        return str(View(self))

    def is_valid(self):
        # TODO
        # special_numbers = [6, 8]
        # for coordinate, tile in self.items():
        #     if tile.number in special_numbers:
        #         for other in Coordinate.get_valid_neighbors(self.size, coordinate):
        #             if self.board[other].number in special_numbers:
        #                 return False
        return True

    def shuffle(self):

        # Reset the board
        self.center_tiles = dict()
        self.border_tiles = dict()

        # Get a list of all resource coordinates
        coordinates = Coordinate.get_valid_coordinates(self.size)

        # Generate the resources and numbers for the board
        res_generator = yield_next_resource()
        num_generator = yield_next_number()
        resources = []
        for coordinate in coordinates:
            resources.append(next(res_generator))
        numbers = []
        for resource in resources:
            if resource is not Resource.DESERT:
                numbers.append(next(num_generator))

        # Lazy way to disperse red numbers
        for i in range(100):

            # Shuffle everything
            shuffle(coordinates)
            shuffle(resources)
            shuffle(numbers)

            # Populate the board
            res_index = 0
            num_index = 0
            for coordinate in coordinates:
                resource = resources[res_index]
                res_index += 1
                number = None
                if resource is not Resource.DESERT:
                    number = numbers[num_index]
                    num_index += 1
                self.center_tiles[coordinate] = Terrain(resource, number)

            # Check the validity of the board
            if self.is_valid():
                break

        # Populate the ports 
        for i, coordinate in enumerate(Coordinate.get_border_coordinates(self.size)):
            self.border_tiles[coordinate] = Harbor(None, Orientation(i % 6))
