from color import Color
from graphics import (
    BUILDING_PLACEHOLDER,
    NUMBER_PLACEHOLDER,
    RESOURCE_PLACEHOLDER,
    ROAD_PLACEHOLDERS,
    TILE_LINES,
)
from resource import Resource


class Tile(object):

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
        assert number in {2, 3, 4, 5, 6, 8, 9, 10, 11, 12}
        self.resource = resource
        self.number = number

    def __str__(self, fancy=True):
        return '\n'.join(
            ''.join(chars for chars in line)
            for line in self.chars()
        )

    def chars(self, fancy=True):
        """ Matrix of the string representation
        """
        string = '\n'.join(TILE_LINES)
        string = string.replace(
            RESOURCE_PLACEHOLDER,
            self.resource.char,
        )
        string = string.replace(
            NUMBER_PLACEHOLDER,
            str(self.number).zfill(2),
        )

        chars = [
            [char for char in line]
            for line in string.split('\n')
        ]

        if fancy:
            for row in range(len(chars)):
                for col in range(len(chars[row])):
                    chars[row][col] = chars[row][col].replace(
                        self.resource.char,
                        self.resource.color.fore(self.resource.char),
                    )
                    chars[row][col] = chars[row][col].replace(
                        BUILDING_PLACEHOLDER,
                        Color.GRAY.fore(BUILDING_PLACEHOLDER),
                    )
                    for road_placeholder in ROAD_PLACEHOLDERS:
                        chars[row][col] = chars[row][col].replace(
                            road_placeholder,
                            Color.GRAY.fore(road_placeholder),
                    )

        return chars
