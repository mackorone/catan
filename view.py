from color import Color
from const import (
    NUM_CORNERS,
    NUM_EDGES,
)


# TODO: MACK - simplify this
BUILDING_SPACES = [
    [(2, 9)],
    [(0, 7)],
    [(0, 2)],
    [(2, 0)],
    [(4, 2)],
    [(4, 7)],
]

# TODO: MACK - simplify this
NUMBER_SPACES = [
    [(2, 4), (2, 5)],
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


def tile_grid(tile):
    tile_grid = replace_buildings(tile, TILE_TEMPLATE)
    tile_grid = replace_resources(tile, tile_grid)
    tile_grid = replace_numbers(tile, tile_grid)
    tile_grid = replace_paths(tile, tile_grid)
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


def replace_numbers(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for spaces in NUMBER_SPACES:
        number_string = (
            str(tile.number).zfill(len(spaces))
            if tile.number else '  '
        )
        for row, col in spaces:
            index = col - min(spaces)[1]
            tile_grid[row][col] = number_string[index]
    return tile_grid


def replace_buildings(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for corner, spaces in enumerate(BUILDING_SPACES):
        for row, col in spaces:
            building = tile.get_building(corner)
            if building:
                tile_grid[row][col] = (
                    building.player.color.fore(str(building.multiplier))
                )
            else:
                tile_grid[row][col] = Color.GRAY.fore(tile_grid[row][col])
    return tile_grid


def replace_paths(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for edge, spaces in enumerate(ROAD_SPACES):
        for row, col in spaces:
            # TODO: MACK - not always gray
            tile_grid[row][col] = Color.GRAY.fore(tile_grid[row][col])
    return tile_grid
    


class View(object):

    def __init__(self, board):
        self.__board = board

    def __str__(self, fancy=True):
        return grid_to_str(self.grid(fancy))

    # TODO: MACK - refactor this ugly logic
    def grid(self, fancy=True):

        tile_height = len(TILE_TEMPLATE)
        tile_narrow = len(''.join(TILE_TEMPLATE[0]).strip())
        tile_wide = len(''.join(TILE_TEMPLATE[len(TILE_TEMPLATE) // 2]).strip())

        total_height = (tile_height - 1) * self.__board.height + 1
        total_width = (
            (self.__board.width // 2 + 1) * (tile_wide   - 1) +
            (self.__board.width // 2    ) * (tile_narrow - 1) + 1
        )
        grid = [
            [' ' for i in range(total_width)]
            for j in range(total_height)
        ]

        for i, row in enumerate(self.__board):
            for j, tile in enumerate(row):

                if i <= self.__board.width // 2:
                    spaces_from_top = (i + j) * (tile_height // 2)
                else:
                    spaces_from_top = (
                        ((self.__board.width // 2 + j) * (tile_height // 2)) +
                        ((i - (self.__board.width // 2)) * (tile_height - 1))
                    )

                if i < self.__board.width // 2:
                    spaces_from_left = (
                        ((self.__board.width // 2) - i + j) *
                        ((tile_wide + tile_narrow) // 2 - 1)
                    )
                else:
                    spaces_from_left = (
                        j * ((tile_wide + tile_narrow) // 2 - 1)
                    )

                tile_g = tile_grid(tile)
                for tile_i, tile_line in enumerate(tile_g):
                    for tile_j, char in enumerate(tile_line):
                        if char != ' ':
                            row = grid[spaces_from_top + tile_i]
                            row[spaces_from_left + tile_j] = char
                    
        return grid
