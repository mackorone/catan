from collections import namedtuple


class Size(namedtuple('Size', ['height', 'width'])):
    def __init__(self, height, width):
        assert 1 <= height
        assert 1 <= width
        assert width % 2 == 1
        assert width < height * 2
