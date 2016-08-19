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


class TileGraphic(object):

    def __init__(self, tile):
        self._tile = tile

    def __str__(self, fancy=True):
        return grid_to_str(self.grid(fancy=fancy))

    @staticmethod
    def _make_fancy(grid, resource):
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

    @staticmethod
    def _space_or_char(tile, number):
        if tile.number and abs(7 - tile.number) <= number:
            return tile.resource.char
        return ' '

    def grid(self, fancy=False):
        string = grid_to_str(TILE_GRID)
        for number in RESOURCE_PLACEHOLDERS:
            string = string.replace(
                str(number),
                TileGraphic._space_or_char(self._tile, number),
            )
        string = string.replace(
            NUMBER_PLACEHOLDER,
            str(self._tile.number).zfill(2) if self._tile.number else '  ',
        )
        grid = str_to_grid(string)
        if fancy:
            grid = TileGraphic._make_fancy(grid, self._tile.resource)
        return grid
