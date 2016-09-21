from building import (
    City,
    Settlement,
)
from error import (
    InvalidCityError,
    InvalidCoordinateError,
    InvalidSettlementError,
)
from generate import generate_board
from intersection import (
    get_intersection_group,
    get_adjacent_intersection_groups,
)


class Board(object):
    """ Model of the game board

    Essentially just a wrapper for a map from Coordinates to Tiles
    """
    def __init__(self: 'Board', size: 'Size'):
        self.__size = size
        self.__board = generate_board(size)

    def __iter__(self: 'Board'):
        return iter(self.__board.items())

    @property
    def size(self: 'Board'):
        return self.__size

    def _validate_new_building(
        self: 'Board',
        intersection: 'Intersection',
        building: 'Building',
    ):
        if intersection.coordinate not in self.__board:
            raise InvalidCoordinateError

    def _validate_new_settlement(
        self: 'Board',
        intersection: 'Intersection',
        settlement: 'Settlement',
    ):
        # Perform validate that pertains to all buildings
        self._validate_new_building(intersection, settlement)

        # Ensure that nothing is currently in that location
        tile = self.__board[intersection.coordinate]
        if tile.get_building(intersection.corner):
            raise InvalidSettlementError(
                'Building already exists at {}'.format(intersection)
            )

        # Enforce the distance rule
        for group in get_adjacent_intersection_groups(
            self.__size,
            intersection,
        ):
            for adjacent_intersection in group:
                adjacent_tile = self.__board[adjacent_intersection.coordinate]
                if adjacent_tile.get_building(adjacent_intersection.corner):
                    raise InvalidSettlementError(
                        '{} failed the distance rule because a building already'
                        ' exists at {}'.format(
                            intersection,
                            adjacent_intersection
                        )
                    )

    def _validate_new_city(
        self: 'Board',
        intersection: 'Intersection',
        city: 'City',
    ):
        # Perform validate that pertains to all buildings
        self._validate_new_building(intersection, city)

        # Retrieve the existing building
        existing_building = (
            self.__board[intersection.coordinate]
                .get_building(intersection.corner)
        )

        # Ensure that a settlement is currently in that location
        if not isinstance(existing_building, Settlement):
            raise InvalidCityError(
                'No settlement exists at {}'.format(intersection)
            )

        # Ensure the the settlement is owned by the correct player
        if existing_building.player != city.player:
            raise InvalidCityError(
                'The settlement at {} is owned by {}, not {}'.format(
                    intersection,
                    str(existing_building.player),
                    str(city.player),
                )
            )

    def _build_building(
        self: 'Board',
        intersection: 'Intersection',
        building: 'Building',
    ):
        for intersection in get_intersection_group(self.__size, intersection):
            tile = self.__board[intersection.coordinate]
            tile.build(intersection.corner, building)

    def build_city(
        self: 'Board',
        intersection: 'Intersection',
        player: 'Player',
    ):
        city = City(player)
        self._validate_new_city(intersection, city)
        self._build_building(intersection, city)

    def build_settlement(
        self: 'Board',
        intersection: 'Intersection',
        player: 'Player',
    ):
        settlement = Settlement(player)
        self._validate_new_settlement(intersection, settlement)
        self._build_building(intersection, settlement)

    def build_road(self: 'Board'):
        raise NotImplementedError
