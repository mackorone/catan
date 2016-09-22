from collections import namedtuple
from coordinate import (
    Coordinate,
)


class Path(namedtuple('Path', ['row', 'column', 'edge'])):
    """ Represents a location where a road can be placed
    """
    @property
    def coordinate(self):
        return Coordinate(self.row, self.column)
