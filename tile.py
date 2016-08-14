from graphics import (
    BUILDING_PLACEHOLDER,
    NUMBER_PLACEHOLDER,
    RESOURCE_PLACEHOLDER,
    ROAD_PLACEHOLDERS,
    TILE_LINES,
)
from color import Color
from resource import Resource


class Tile(object):

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
        assert number in {2, 3, 4, 5, 6, 8, 9, 10, 11, 12}
        self.resource = resource
        self.number = number

    def __str__(self, fancy=True):

        string = '\n'.join(TILE_LINES)
        string = string.replace(
            RESOURCE_PLACEHOLDER,
            self.resource.char,
        )
        string = string.replace(
            NUMBER_PLACEHOLDER,
            str(self.number).zfill(2),
        )

        if fancy:
            string = string.replace(
                self.resource.char,
                self.resource.color.fore(self.resource.char),
            )
            string = string.replace(
                BUILDING_PLACEHOLDER,
                Color.GRAY.fore(BUILDING_PLACEHOLDER),
            )
            for road_placeholder in ROAD_PLACEHOLDERS:
                string = string.replace(
                    road_placeholder,
                    Color.GRAY.fore(road_placeholder),
            )

        return string
