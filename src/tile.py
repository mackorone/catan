from collections import namedtuple


Terrain = namedtuple('Terrain', ['resource', 'number'])
Terrain.__new__.__defaults__ = (None, None)


Harbor = namedtuple('Harbor', ['resource', 'orientation'])
Harbor.__new__.__defaults__ = (None, None)
