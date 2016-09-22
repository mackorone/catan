from color import Color
from const import (
    NUM_CORNERS,
    NUM_EDGES,
)


BUILDING_SPACES = [
    (2, 9),
    (0, 7),
    (0, 2),
    (2, 0),
    (4, 2),
    (4, 7),
]

NUMBER_SPACES = [
    (2, 4),
    (2, 5)
]

RESOURCE_SPACES = [
    [(1, 5), (3, 4)],
    [(1, 4), (3, 5)],
    [(1, 6), (3, 3)],
    [(1, 3), (3, 6)],
    [(2, 2), (2, 7)],
]

ROAD_SPACES = [
    [(1, 8),       ],
    [(0, 4), (0, 5)],
    [(1, 1),       ],
    [(3, 1),       ],
    [(4, 4), (4, 5)],
    [(3, 8),       ],
]

TILE_TEMPLATE = [
   list('  + -- +  '),
   list(' /      \ '),
   list('+        +'),
   list(' \      / '),
   list('  + -- +  '),
]


assert len(BUILDING_SPACES) == NUM_CORNERS
assert len(ROAD_SPACES) == NUM_EDGES


def copy_grid(grid):
    return [[c for c in row] for row in grid]


def grid_to_str(grid):
    return '\n'.join(''.join(row) for row in grid)


def str_to_grid(string):
    return [[c for c in line] for line in string.split('\n')]


def get_tile_grid(tile):
    tile_grid = copy_grid(TILE_TEMPLATE)
    tile_grid = replace_buildings(tile, tile_grid)
    tile_grid = replace_numbers(tile, tile_grid)
    tile_grid = replace_resources(tile, tile_grid)
    tile_grid = replace_roads(tile, tile_grid)
    return tile_grid


def replace_buildings(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for corner, (row, col) in enumerate(BUILDING_SPACES):
        building = tile.get_building(corner)
        if building:
            tile_grid[row][col] = (
                building.player.color.back(
                    Color.BLACK.fore(
                        str(building.multiplier)
                    )
                )
            )
        else:
            tile_grid[row][col] = Color.GRAY.fore(tile_grid[row][col])
    return tile_grid


def replace_numbers(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    number_string = (
        str(tile.number).zfill(len(NUMBER_SPACES))
        if tile.number else '  '
    )
    for row, col in NUMBER_SPACES:
        index = col - min(NUMBER_SPACES)[1]
        tile_grid[row][col] = number_string[index]
    return tile_grid


def replace_resources(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for value, spaces in enumerate(RESOURCE_SPACES):
        for row, col in spaces:
            if tile.number and abs(7 - tile.number) <= value + 1:
                tile_grid[row][col] = (
                    tile.resource.color.fore(
                        tile.resource.char
                    )
                )
    return tile_grid


def replace_roads(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for edge, spaces in enumerate(ROAD_SPACES):
        for row, col in spaces:
            # TODO: not always gray
            tile_grid[row][col] = Color.GRAY.fore(tile_grid[row][col])
    return tile_grid
    

class View(object):

    def __init__(self, board):
        self.__board = board

    def __str__(self):
        return grid_to_str(self.get_board_grid())

    def get_board_grid(self):

        # Retrieve the height and width of the board
        height = self.__board.size.height
        width = self.__board.size.width

        # The number of characters tall and wide for the tile grid
        tile_grid_height = len(TILE_TEMPLATE)
        tile_grid_narrow = len(''.join(TILE_TEMPLATE[0]).strip())
        tile_grid_wide = len(''.join(TILE_TEMPLATE[2]).strip())

        # The number of characters tall and wide for the board grid
        total_grid_height = (tile_grid_height - 1) * height + 1
        total_grid_width = (
            (width // 2 + 1) * (tile_grid_wide   - 1) +
            (width // 2    ) * (tile_grid_narrow - 1) + 1
        )

        # Create a 2D array of empty spaces, large enough to
        # contain all characters for all tiles (but no larger)
        board_grid = [
            [' ' for i in range(total_grid_width)]
            for j in range(total_grid_height)
        ]

        # For all coordinates ...
        for coordinate, tile in self.__board:

            # ... determine some intermediate values ...
            sum_ = coordinate.row + coordinate.column
            difference = coordinate.row - coordinate.column

            # ... and use them to figure the location of the upper
            # left corner of the tile grid within the board grid ...
            spaces_from_top = sum_ * (tile_grid_height // 2)
            spaces_from_left = (
                ((width // 2) - difference) *
                ((tile_grid_wide + tile_grid_narrow) // 2 - 1)
            )

            # ... and then replace the blank characters in the board
            # grid with the correct characters from the tile grid
            tile_grid = get_tile_grid(tile)
            for i, tile_line in enumerate(tile_grid):
                for j, char in enumerate(tile_line):
                    if char != ' ':
                        row = board_grid[spaces_from_top + i]
                        row[spaces_from_left + j] = char
                
        return board_grid
