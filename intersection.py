from collections import namedtuple
from coordinate import Coordinate
from size import Size


class Intersection(namedtuple('Intersection', ['row', 'column', 'corner'])):
    """ Represents a location where a building can be placed
    """
    def __new__(self, row, column, corner):
        return super().__new__(Intersection, row, column, corner)

    @property
    def coordinate(self):
        return Coordinate(self.row, self.column)

    @classmethod
    def from_coordinate(cls, coordinate, corner):
        return Intersection(coordinate.row, coordinate.column, corner)
        

def get_intersection_group(size, intersection):
    # TODO: Add a docstring here
    assert isinstance(size, Size) 
    assert isinstance(intersection, Intersection) 
    # TODO: return all equivalent vertices here
    return {intersection}


def get_adjacent_intersection_groups(size, intersection):
    # TODO: Add a docstring here, implement this
    return {}
