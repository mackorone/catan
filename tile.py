from color import Color
from graphics import (
    NUMBER_PLACEHOLDER,
    RESOURCE_PLACEHOLDER,
    TILE_GRID,
    grid_to_str,
    make_fancy,
    str_to_grid,
)
from resource import Resource


class Tile(object):

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
        assert number in {
            None, 
            2,  3,  4,  5,  6,
            8,  9, 10, 11, 12,
        }
        self.resource = resource
        self.number = number

    def __str__(self, fancy=True):
        return grid_to_str(self.grid(fancy=fancy))

    def grid(self, fancy=False):
        string = grid_to_str(TILE_GRID)
        string = string.replace(
            RESOURCE_PLACEHOLDER,
            self.resource.char,
        )
        string = string.replace(
            NUMBER_PLACEHOLDER,
            str(self.number).zfill(2) if self.number else '  ',
        )
        grid = str_to_grid(string)
        if fancy:
            grid = make_fancy(grid, self.resource)
        return grid
