from collections import namedtuple
from resource import Resource


class InvalidTileError(Exception):
    pass


class Tile(namedtuple('Tile', ['resource', 'number'])):
    def __init__(self, resource, number):
        if (resource is Resource.DESERT) != (number is None):
            raise InvalidTileError(
                'Resource={}, Number={}'.format(
                    resource,
                    number,
                )
            )
