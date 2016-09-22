from collections import namedtuple
from coordinate import (
    Coordinate,
    get_valid_neighbors,
)


class Intersection(namedtuple('Intersection', ['row', 'column', 'corner'])):
    """ Represents a location where a building can be placed
    """
    @property
    def coordinate(self):
        return Coordinate(self.row, self.column)


def get_intersection_group(
    size: 'Size',
    intersection: 'Intersection',
):
    """ Returns the given intersection's equivalence class
    """

    # The indices of these tuples correspond to the corner
    offsets = [
        (-1,  0), (-1, -1), ( 0, -1),
        ( 1,  0), ( 1,  1), ( 0,  1),
    ]
    
    # The other two potential members of the group
    other_potential_group_members = set()
    for k in [-1, 0]:
        i, j = offsets[intersection.corner + k]
        other_potential_group_members.add(
            Intersection(
                row=intersection.row + i,
                column=intersection.column + j,
                corner=(intersection.corner + 4 + 2 * k) % 6,
            )
        )

    # The valid neighbors of the intersection's coordinate
    valid_neighbors = get_valid_neighbors(size, intersection.coordinate)

    # The actual members of the intersection group
    actual_group_members = set([intersection])
    for member in other_potential_group_members:
        if member.coordinate in valid_neighbors:
            actual_group_members.add(member)

    return actual_group_members


def get_adjacent_intersection_groups(
    size: 'Size',
    intersection: 'Intersection',
):
    """ Returns the equivalence classes for all adjacent intersections
    """

    adjacent_intersection_groups = set()
    for member in get_intersection_group(size, intersection):
        for k in [-1, 1]:
            adjacent_intersection_groups.add(
                frozenset(
                    get_intersection_group(
                        size=size,
                        intersection=Intersection(
                            row=member.row,
                            column=member.column,
                            corner=(member.corner + k) % 6,
                        )
                    )
                )
            )

    return adjacent_intersection_groups
