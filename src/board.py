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
       None,
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
        special_numbers = [6, 8]
        for coordinate, tile in self.tiles.items():
            if tile.number in special_numbers:
                for other in coordinate.get_valid_neighbors(self.size):
                    if self.tiles[other].number in special_numbers:
                        return False
        return True

    def shuffle(self):

        # Reset the board
        self.tiles = dict()

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
            if resource is not None:
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
                if resource is not None:
                    number = numbers[num_index]
                    num_index += 1
                self.tiles[coordinate] = Terrain(resource, number)

            # Check the validity of the board
            if self.is_valid():
                break

        # Populate the ports 
        for i, coordinate in enumerate(Coordinate.get_border_coordinates(self.size)):
            # TODO: upforgrabs
            # These are hard-coded for a normal sized board;
            # harbor tiles should work for all sized boards
            harbors = {
                (-1,  0): (           None, Orientation.SOUTH     ),
                (-1,  2): (           None, Orientation.SOUTH_WEST),
                ( 0, -1): ( Resource.SHEEP, Orientation.SOUTH     ),
                ( 1,  4): ( Resource.BRICK, Orientation.NORTH_WEST),
                ( 2, -1): (           None, Orientation.SOUTH_EAST),
                ( 3,  5): (Resource.LUMBER, Orientation.NORTH_WEST),
                ( 4,  1): (   Resource.ORE, Orientation.NORTH_EAST),
                ( 5,  3): ( Resource.WHEAT, Orientation.NORTH_EAST),
                ( 5,  5): (           None, Orientation.NORTH     ),
            }
            resource, orientation = harbors.get(
                (coordinate.row, coordinate.column),
                (None, None),
            )
            self.tiles[coordinate] = Harbor(resource, orientation)
