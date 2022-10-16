from collections import namedtuple


class InvalidSizeError(Exception):
    pass


class Size(namedtuple('Size', ['height', 'width'])):
    def __init__(self, height, width):
        if not (
            1 <= height and
            1 <= width and
            width % 2 == 1 and
            width < height * 2
        ):
            raise InvalidSizeError(
                'Height={}, Width={}'.format(
                    height,
                    width,
                )
            )
