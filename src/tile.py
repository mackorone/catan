from building import Building
from const import (
    NUM_CORNERS,
    NUM_EDGES,
)
from error import (
    InvalidCornerError,
    InvalidTileError,
)
from pieces import NUMBERS
from resource import Resource
from typing import Union


class Tile(object):
    """
      2 -- 1       +  1 +    
     / tile \     2 tile 0   
    3 corner 0   +  edge  +  
     \  #s  /     3  #s  5   
      4 -- 5       + 4  +    
    """

    def __init__(
        self: 'Tile',
        resource: 'Resource',
        number: Union[int, None],
    ):
        if resource == Resource.DESERT:
            if number is not None:
                raise InvalidTileError(
                    'A {} tile must not have a numeric value'.format(resource)
                )
        else:
            if number not in NUMBERS:
                raise InvalidTileError(
                    'A {} tile must have a numeric value'.format(resource)
                )
        
        self.__resource = resource
        self.__number = number
        self.__edges = [None] * NUM_EDGES
        self.__corners = [None] * NUM_CORNERS

    @property
    def resource(self):
        return self.__resource

    @property
    def number(self):
        return self.__number

    def build_building(self, corner: int, building: 'Building'):
        if not 0 <= corner < NUM_CORNERS:
            raise InvalidCornerError(
                # TODO: put a proper error string here
            )
        self.__corners[corner] = building

    def get_building(self, corner: int):
        if not 0 <= corner < NUM_CORNERS:
            raise InvalidCornerError(
                # TODO: put a proper error string here
            )
        return self.__corners[corner]
