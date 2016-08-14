from color import Color


BUILDING_PLACEHOLDER = '+'
NUMBER_PLACEHOLDER = '##'
RESOURCE_PLACEHOLDER = '*'
ROAD_PLACEHOLDERS = {'-', '/', '\\'}
TILE_GRID = [
   list('  + -- +  '),
   list(' / **** \ '),
   list('+ * ## * +'),
   list(' \ **** / '),
   list('  + -- +  '),
]


def grid_to_str(grid):
    return '\n'.join(''.join(row) for row in grid)


def str_to_grid(string):
    return [
        [char for char in line]
        for line in string.split('\n')
    ]


def make_fancy(grid, resource):
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
