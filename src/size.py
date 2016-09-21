from collections import namedtuple
from error import InvalidSizeError


class Size(namedtuple('Size', ['height', 'width'])):
    def __init__(self, height, width):
        # TODO: Replace with InvalidSizeError
        assert 1 <= height
        assert 1 <= width
        assert width % 2 == 1
        assert width < height * 2
