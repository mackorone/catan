from city import City
from const import (
    NUM_CORNERS,
    NUM_EDGES,
)
from resource import Resource
from settlement import Settlement


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
        # TODO: MACK - this should be based on the dice...
        assert number in {
            None, 
            2,  3,  4,  5,  6,
            8,  9, 10, 11, 12,
        }
        assert (
            number
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

    def build_city(self, corner, player):
        assert 0 <= corner < NUM_CORNERS
        self.__corners[corner] = City(player)

    def build_settlement(self, corner, player):
        assert 0 <= corner < NUM_CORNERS
        self.__corners[corner] = Settlement(player)

    def get_building(self, corner):
        assert 0 <= corner < NUM_CORNERS
        return self.__corners[corner]
