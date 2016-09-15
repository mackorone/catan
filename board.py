from building import (
    Building,
    City,
    Settlement,
)
from generate import generate_board
from intersection import (
    Intersection,
    get_intersection_group,
    get_adjacent_intersection_groups,
)


class Board(object):
    """ Model of the game board

    Essentially just a wrapper for a map from Coordinates to Tiles
    """
    def __init__(self, size):
        self.__size = size
        self.__board = generate_board(size)

    def __iter__(self):
        return iter(self.__board.items())

    @property
    def size(self):
        return self.__size

    def _validate_new_building(self, intersection, building):
        assert isinstance(building, Building)
        assert intersection.coordinate in self.__board

    def _validate_new_settlement(self, intersection, settlement):

        # Perform all validation that applies to all building types
        assert isinstance(settlement, Settlement)
        self._validate_new_building(intersection, settlement)

        # Ensure that nothing is currently in that location
        assert not (
            self.__board[intersection.coordinate]
                .get_building(intersection.corner)
        )

        # Enforce the distance rule
        for group in get_adjacent_intersection_groups(
            self.__size,
            intersection,
        ):
            for adjacent_intersection in group:
                assert not (
                    self.__board[adjacent_intersection.coordinate]
                        .get_building(adjacent_intersection.corner)
                )

    def _validate_new_city(self, intersection, city):

        # Perform all validation that applies to all building types
        assert isinstance(intersection, Intersection)
        self._validate_new_building(intersection, city)

        # Retrieve the existing building
        existing_building = (
            self.__board[intersection.coordinate]
                .get_building(intersection.corner)
        )

        # Ensure that a settlement is currently in that location
        assert isinstance(existing_building, Settlement)
        
        # Ensure the the settlement is owned by the correct player
        assert existing_building.player == city.player

    def _build_building(self, intersection, building):
        for intersection in get_intersection_group(self.__size, intersection):
            tile = self.__board[intersection.coordinate]
            tile.build(intersection.corner, building)

    def build_city(self, intersection, player):
        city = City(player)
        self._validate_new_city(intersection, city)
        self._build_building(intersection, city)

    def build_settlement(self, intersection, player):
        settlement = Settlement(player)
        self._validate_new_settlement(intersection, settlement)
        self._build_building(intersection, settlement)

    def build_road(self):
        raise NotImplementedError
