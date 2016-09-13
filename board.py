from const import NUM_CORNERS
from coordinate import Coordinate
from pieces import (
    HEXAGONS,
    NUMBERS,
)
from pprint import pprint
from random import shuffle
from resource import Resource
from tile import Tile


class Board(object):
    """ Model of the game board

    Rows go from the upper left to the lower right, i.e.:

                   <------- width ------- >
   
    ^                       + -- + 
    |                      /      \ 
    |                + -- +   00   + -- +
    |               /      \      /      \ 
    |         -    +   10   + -- +   01   +    -
                    \      /      \      /       
  height    -   20   + -- +   11   + -- +   02   -
                    /      \      /      \       
    |         -    +   21   + -- +   12   +    -
    |               \      /      \      /       
    |                + -- +   22   + -- +         
    |                      \      /              
    v                       + -- +              

    Note that spaces (0, 2) and (2, 0) aren't valid, but
    the numbering reflects their hypothetical existence.
    """
    def __init__(self, height, width):

        # Assert valid size
        assert 1 <= height
        assert 1 <= width
        assert width % 2 == 1
        assert width < height * 2

        # Initialize the members
        self.__height = height
        self.__width = width
        self.__board = Board._generate(height, width)
        pprint(self.__board)
        exit(0)

    def __iter__(self):
        return iter(self.__board.items())

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

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

    def build_city(self, row, column, corner, player):
        raise NotImplementedError

    def build_settlement(self, row, column, corner, player):
        assert row < len(self.__board)
        assert column < len(self.__board[row])
        # TODO: Enforce two-hop rule
        assert not self.__board[row][column].get_building(corner)

        # TODO: MACK - build neighboring settlements
        self.__board[row][column].build_settlement(corner, player)
        #print(row, column, corner)
        # for ((other_row, other_column), other_corner) in (
        #     self._get_neighboring_tiles(row, column, corner)
        # ):
        #     #print(other_row, other_column, other_corner)
        #     self.__board[other_row][other_column].build_settlement(other_corner, player)

    def build_road(self):
        raise NotImplementedError

    @staticmethod
    def _generate(height, width):

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
        for coordinate in Board._get_coordinates(height, width):
            resource = hexagons[res_index]
            res_index += 1
            if resource == Resource.DESERT:
                number = None
            else:
                number = numbers[num_index]
                num_index += 1      
            board[coordinate] = Tile(resource, number)
        return board

    @staticmethod
    def _get_coordinates(height, width):
        coordinates = set()
        for row in range(height):
            coordinates.add(Coordinate(row, row))
            for i in range(
            # effective_row_number = (
            #     row_number
            #     if row_number <= (height + 1) // 2 - 1
            #     else height - 1 - row_number
            # )
            # return min(
            #     min(width, height),
            #     (width // 2 + 1) + effective_row_number,
            # )
        return coordinates
