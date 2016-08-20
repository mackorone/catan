""" Config for game pieces, currently hardcoded
"""


from resource import Resource


HEXAGONS = {
    Resource.BRICK: 3,
    Resource.DESERT: 1,
    Resource.LUMBER: 4,
    Resource.ORE: 3,
    Resource.SHEEP: 4,
    Resource.WHEAT: 4,
}


NUMBERS = {
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    8: 2,
    9: 2,
    10: 2,
    11: 2,
    12: 1,
}


PORTS = {
    Resource.BRICK: 1,
    Resource.LUMBER: 1,
    Resource.ORE: 1,
    Resource.SHEEP: 1,
    Resource.WHEAT: 1,
    None: 4,
}
