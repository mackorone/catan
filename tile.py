from resource import Resource


class Tile(object):

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
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

    @property
    def resource(self):
        return self.__resource

    @property
    def number(self):
        return self.__number
