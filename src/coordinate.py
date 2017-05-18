from collections import namedtuple


class InvalidCoordinateError(Exception):
    pass


class Coordinate(namedtuple('Coordinate', ['row', 'column'])):
    """ Represents a board coordinate

    Here are the coordinates of a standard Catan board:

                                  + -- +                
                                 /      \               
                           + -- +   00   + -- +         
                          /      \      /      \        
                    + -- +   10   + -- +   01   + -- +  
                   /      \      /      \      /      \ 
             -    +   20   + -- +   11   + -- +   02   +    -
                   \      /      \      /      \      / 
      -    -   30   + -- +   21   + -- +   12   + -- +   03   -    -
                   /      \      /      \      /      \ 
    -   40   -    +   31   + -- +   22   + -- +   13   +    -   04   -
                   \      /      \      /      \      / 
      -    -   41   + -- +   32   + -- +   23   + -- +   14   -    -
                   /      \      /      \      /      \ 
             -    +   42   + -- +   33   + -- +   24   +    -
                   \      /      \      /      \      / 
                    + -- +   43   + -- +   34   + -- +  
                          \      /      \      /        
                           + -- +   44   + -- +
                                 \      /
                                  + -- + 

    Note that the first digit represents the row and the second digit
    represents the column. Also note that (0, 3), (0, 4), (1, 4), (3, 0),
    (4, 0), and (4, 1) are invalid coordinates, but they're still counted in
    the coordinate numbering scheme. This helps to keep things consistent for
    mazes of different sizes.
    """


def get_all_coordinates(height):
    """ All possibly valid coordinates for a board of given height
    """
    return [
        Coordinate(row, column)
        for row in range(height)
        for column in range(height)
    ]


def get_valid_coordinates(size):
    """ The valid coordinates for a board of given size
    """
    all_coordinates = get_all_coordinates(size.height)
    return [
        coordinate for
        coordinate in all_coordinates if
        abs(coordinate.row - coordinate.column) <= size.width // 2
    ]


def get_all_neighbors(coordinate):
    """ All possible neighbors for a given coordinate

    Note that the neighbors might be invalid coordinates
    """
    return [
        Coordinate(coordinate.row + i, coordinate.column + j)
        for (i, j) in [
            (-1, -1), (-1,  0), ( 0, -1),
            ( 0,  1), ( 1,  0), ( 1,  1),
        ]
    ]


def get_valid_neighbors(size, coordinate):
    """ All valid neighbors for a given board size and coordinate
    """
    valid_coordinates = set(get_valid_coordinates(size))
    if coordinate not in valid_coordinates:
        raise InvalidCoordinateError(
            '{} is not in {}'.format(
                coordinate,
                valid_coordinates,
            )
        )

    all_neighbors = get_all_neighbors(coordinate)
    return [
        neighbor for
        neighbor in all_neighbors if
        neighbor in valid_coordinates
    ]
