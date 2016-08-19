from color import Color


BUILDING_PLACEHOLDER  = '+'
NUMBER_PLACEHOLDER    = '##'
RESOURCE_PLACEHOLDERS = range(1, 6)
ROAD_PLACEHOLDERS     = list('\-/')

TILE_GRID = [
   list('  + -- +  '),
   list(' / 4213 \ '),
   list('+ 5 ## 5 +'),
   list(' \ 3124 / '),
   list('  + -- +  '),
]


def grid_to_str(grid):
    return '\n'.join(''.join(row) for row in grid)


def str_to_grid(string):
    return [
        [char for char in line]
        for line in string.split('\n')
    ]


def fancy_tile_grid(grid, resource):
    """ Adds color to the tile grid
    """
    fancy = [
        [char for char in row]
        for row in grid
    ]

    for row in range(len(fancy)):
        for col in range(len(fancy[row])):
            if resource.char != ' ':
                fancy[row][col] = fancy[row][col].replace(
                    resource.char,
                    resource.color.fore(resource.char),
                )
            fancy[row][col] = fancy[row][col].replace(
                BUILDING_PLACEHOLDER,
                Color.GRAY.fore(BUILDING_PLACEHOLDER),
            )
            for road_placeholder in ROAD_PLACEHOLDERS:
                fancy[row][col] = fancy[row][col].replace(
                    road_placeholder,
                    Color.GRAY.fore(road_placeholder),
            )

    return fancy


def space_or_char(tile, number):
    if tile.number and abs(7 - tile.number) <= number:
        return tile.resource.char
    return ' '


def tile_grid(tile, fancy=True):
    string = grid_to_str(TILE_GRID)
    for number in RESOURCE_PLACEHOLDERS:
        string = string.replace(
            str(number),
            space_or_char(tile, number),
        )
    string = string.replace(
        NUMBER_PLACEHOLDER,
        str(tile.number).zfill(2) if tile.number else '  ',
    )
    grid = str_to_grid(string)
    if fancy:
        grid = fancy_tile_grid(grid, tile.resource)
    return grid


class UI(object):

    def __init__(self, board):
        self.__board = board

    def __str__(self, fancy=True):
        return grid_to_str(self.grid(fancy))

    def grid(self, fancy=True):

        tile_height = len(TILE_GRID)
        tile_narrow = len(''.join(TILE_GRID[0]).strip())
        tile_wide = len(''.join(TILE_GRID[len(TILE_GRID) // 2]).strip())

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

                for tile_i, tile_line in enumerate(tile_grid(tile, fancy)):
                    for tile_j, char in enumerate(tile_line):
                        if char != ' ':
                            grid[spaces_from_top + tile_i][spaces_from_left + tile_j] = char
                    
        return grid
