from collections import namedtuple
from size import Size


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
    def __init__(self, row, column):
        assert 0 <= row
        assert 0 <= column


def get_valid_coordinates(size):
    assert isinstance(size, Size)
    coordinates = set()
    for row in range(size.height):
        for column in range(size.height):
            if abs(row - column) <= size.width // 2:
                coordinates.add(Coordinate(row, column))
    return coordinates
