from const import NUM_CORNERS
from coordinate import (
    Coordinate,
    get_valid_coordinates,
    get_valid_neighbors,
)
from pieces import (
    HEXAGONS,
    NUMBERS,
)
from pprint import pprint
from random import shuffle
from resource import Resource
from tile import Tile
from intersection import (
    Intersection,
    get_intersection_group,
    get_adjacent_intersection_groups,
)


class Board(object):
    """ Model of the game board

    Essentially just a wrapper for a map from Coordinates to Tiles
    """
    def __init__(self, size):
        # Initialize the members
        self.__size = size
        self.__board = Board._generate(size)

    def __iter__(self):
        return iter(self.__board.items())

    @property
    def size(self):
        return self.__size

    # TODO: MACK - return points
    # def _get_neighboring_tiles(self, row, column, corner):
    #     # TODO: This isn't correct, because it depends on row
    #     tile_offsets = [
    #         (-1,  0), (-1, -1), ( 0, -1),
    #         ( 1,  0), ( 1,  1), ( 0,  1),
    #     ]
    #     assert len(tile_offsets) == NUM_CORNERS
    #     assert 0 <= corner <= len(tile_offsets)
    #     neighbors = set()
    #     for offset, other_corner in [
    #         (tile_offsets[corner - 1], (corner + 2) % NUM_CORNERS),
    #         (tile_offsets[corner    ], (corner + 4) % NUM_CORNERS),
    #     ]:
    #         other_tile = (row + offset[0], column + offset[1])
    #         if (
    #             0 <= other_tile[0] < self.width and 
    #             0 <= other_tile[1] < self.height
    #         ):
    #             neighbors.add((other_tile, other_corner))
    #     return neighbors

    def build_city(self, intersection, player):
        raise NotImplementedError

    def build_settlement(self, intersection, player):
        # TODO: Ensure connected to a road
        assert isinstance(intersection, Intersection)
        assert intersection.coordinate in self.__board
        assert not self.__board[intersection.coordinate].get_building(intersection.corner)
        for group in get_adjacent_intersection_groups(self.__size, intersection):
            for adjacent_intersection in group:
                assert not self.__board[adjacent_intersection.coordinate].get_building(adjacent_intersection.corner)
        # TODO: Enforce two-hop rule
        for intersection in get_intersection_group(self.__size, intersection):
            self.__board[intersection.coordinate].build_settlement(intersection.corner, player)

    def build_road(self):
        raise NotImplementedError

    # TODO: MACK - move this some place else
    @staticmethod
    def _generate(size):

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
