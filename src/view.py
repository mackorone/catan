from color import Color


CENTER_TILE_TEMPLATE = [
   list('  + -- +  '),
   list(' /      \ '),
   list('+        +'),
   list(' \      / '),
   list('  + -- +  '),
]

BORDER_TILE_TEMPLATE = [
   list('  | -- |  '),
   list(' -      - '),
   list('  |    |  '),
   list(' -      - '),
   list('  | -- |  '),
]

NUMBER_SPACES = [
    (2, 4), (2, 5)
]

PERIMETER_SPACES = [
    (0, 2), (0, 4),
    (0, 5), (0, 7),
    (1, 1), (1, 8),
    (2, 0), (2, 2),
    (2, 7), (2, 9),
    (3, 1), (3, 8),
    (4, 2), (4, 4),
    (4, 5), (4, 7),
]

RESOURCE_SPACES = [
    (1, 3), (1, 4),
    (1, 5), (1, 6),
    (2, 2), (2, 7),
    (3, 3), (3, 4),
    (3, 5), (3, 6),
]


def remove_border_characters(board, coordinate, diff, tile_grid):

    # First, calculate some helper values
    helper_value_one = board.size.width // 2
    helper_value_two = board.size.height - helper_value_one

    # Top vertical ticks
    if (
        coordinate.row == -1 or
        coordinate.column == -1
    ):
        tile_grid[0][2] = ' '
        tile_grid[0][7] = ' '

    # Top horizonal ticks
    else:
        tile_grid[0][4] = ' '
        tile_grid[0][5] = ' '

    # Bottom vertical ticks
    if (
        coordinate.row == board.size.height or
        coordinate.column == board.size.height
    ):
        tile_grid[4][2] = ' '
        tile_grid[4][7] = ' '

    # Bottom horizonal ticks
    else:
        tile_grid[4][4] = ' '
        tile_grid[4][5] = ' '

    # Upper left single tick
    if not (
        coordinate.column == -1 and
        coordinate.row < helper_value_one
    ):
        tile_grid[1][1] = ' '

    # Upper right single tick
    if not (
        coordinate.row == -1 and
        coordinate.column < helper_value_one
    ):
        tile_grid[1][8] = ' '

    # Bottom left single tick
    if not (
        coordinate.row == board.size.height and
        helper_value_two <= coordinate.column
    ):
        tile_grid[3][1] = ' '

    # Bottom right single tick
    if not (
        coordinate.column == board.size.height and
        helper_value_two <= coordinate.row
    ):
        tile_grid[3][8] = ' '

    # Left vertical ticks
    if abs(diff) <= helper_value_one or diff < 0:
        tile_grid[0][2] = ' '
        tile_grid[2][2] = ' '
        tile_grid[4][2] = ' '
    
    # Right vertical ticks
    if abs(diff) <= helper_value_one or 0 < diff:
        tile_grid[0][7] = ' '
        tile_grid[2][7] = ' '
        tile_grid[4][7] = ' '

    return tile_grid


def copy_grid(grid):
    return [[char for char in row] for row in grid]


def grid_to_str(grid):
    return '\n'.join(''.join(row) for row in grid)


def str_to_grid(string):
    return [[c for c in line] for line in string.split('\n')]


def get_tile_grid(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    tile_grid = replace_numbers(tile, tile_grid)
    tile_grid = replace_perimeter(tile, tile_grid)
    tile_grid = replace_resources(tile, tile_grid)
    return tile_grid


def replace_numbers(tile, tile_grid):
    if not tile.number:
        return tile_grid
    tile_grid = copy_grid(tile_grid)
    number_string = str(tile.number).zfill(len(NUMBER_SPACES))
    for row, col in NUMBER_SPACES:
        index = col - min(NUMBER_SPACES)[1]
        tile_grid[row][col] = number_string[index]
    return tile_grid


def replace_perimeter(tile, tile_grid):
    tile_grid = copy_grid(tile_grid)
    for row, col in PERIMETER_SPACES:
        colored = Color.GRAY.apply(tile_grid[row][col])
        tile_grid[row][col] = colored
    return tile_grid


def replace_resources(tile, tile_grid):
    if not tile.resource:
        return tile_grid
    tile_grid = copy_grid(tile_grid)
    for row, col in RESOURCE_SPACES:
        colored = tile.resource.color.apply(tile.resource.char)
        tile_grid[row][col] = colored
    return tile_grid


class View(object):

    def __init__(self, board):
        self.board = board

    def __str__(self):
        return grid_to_str(self.get_board_grid())

    def get_board_grid(self):

        # Add two to the height and width of the
		# board to account for the perimeter tiles
        num_tiles_tall = self.board.size.height + 2
        num_tiles_wide = self.board.size.width + 2

        # The number of characters tall and wide for the tile grid
        tile_grid_height = len(CENTER_TILE_TEMPLATE)
        tile_grid_narrow = len(''.join(CENTER_TILE_TEMPLATE[0]).strip())
        tile_grid_wide = len(''.join(CENTER_TILE_TEMPLATE[2]).strip())

        # The number of characters tall and wide for the board grid
        total_grid_height = (tile_grid_height - 1) * num_tiles_tall + 1
        total_grid_width = (
            (num_tiles_wide // 2 + 1) * (tile_grid_wide   - 1) +
            (num_tiles_wide // 2    ) * (tile_grid_narrow - 1) + 1
        )

        # Create a 2D array of empty spaces, large enough to
        # contain all characters for all tiles (but no larger)
        board_grid = [
            [' ' for i in range(total_grid_width)]
            for j in range(total_grid_height)
        ]

        # For all border and center coordinates ...
        for group in [
            self.board.border_tiles,
            self.board.center_tiles,
        ]:
            for coordinate, tile in group.items():

                # ... determine some intermediate values ...
                # Note: We add +1 here to account for perimeter tiles
                sum_ = (coordinate.row + 1) + (coordinate.column + 1)
                diff = (coordinate.row + 1) - (coordinate.column + 1)
 
                # ... and use them to figure the location of the upper
                # left corner of the tile grid within the board grid ...
                spaces_from_top = sum_ * (tile_grid_height // 2)
                spaces_from_left = (
                    ((num_tiles_wide // 2) - diff) *
                    ((tile_grid_wide + tile_grid_narrow) // 2 - 1)
                )

                # ... then retrieve the base tile grid for the tile ...
                template = (
                    CENTER_TILE_TEMPLATE if
                    group == self.board.center_tiles else
                    remove_border_characters(
                        board=self.board,
                        coordinate=coordinate,
                        diff=diff,
                        tile_grid=copy_grid(BORDER_TILE_TEMPLATE),
                    )
                )

                # ... and then replace the blank characters in the board
                # grid with the correct characters from the tile grid
                tile_grid = get_tile_grid(tile, template)
                for i, tile_line in enumerate(tile_grid):
                    for j, char in enumerate(tile_line):
                        if char != ' ':
                            row = board_grid[spaces_from_top + i]
                            row[spaces_from_left + j] = char

        # Trim extra columns off front and back of the grid
        board_grid = [row[2:-2] for row in board_grid]
        return board_grid
