from building import Building
from const import (
    NUM_CORNERS,
    NUM_EDGES,
)
from pieces import NUMBERS
from resource import Resource


class Tile(object):
    """
      2 -- 1       x  1 x    
     / tile \     2 tile 0   
    3 corner 0   x  edge  x  
     \  #s  /     3  #s  5   
      4 -- 5       x 4  x    
    """

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
        assert (
            number in NUMBERS
            if resource != Resource.DESERT
            else number is None
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

    def build(self, corner, building):
        assert 0 <= corner < NUM_CORNERS
        assert isinstance(building, Building)
        self.__corners[corner] = building

    def get_building(self, corner):
        assert 0 <= corner < NUM_CORNERS
        return self.__corners[corner]
