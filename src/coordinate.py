from collections import namedtuple


class Coordinate(namedtuple('Coordinate', ['row', 'column'])):
    """ Represents a board coordinate

    Here are the coordinates of a standard Catan board:
    
                           --
                        -      -
                    --            --
                 -                    -
             --          + -- +          --
          -             /      \             -
      --          + -- +   00   + -- +          --
                 /      \      /      \
    |      + -- +   10   + -- +   01   + -- +      |
          /      \      /      \      /      \
    |    +   20   + -- +   11   + -- +   02   +    |
          \      /      \      /      \      /
    |      + -- +   21   + -- +   12   + -- +      |
          /      \      /      \      /      \
    |    +   31   + -- +   22   + -- +   13   +    |
          \      /      \      /      \      /
    |      + -- +   32   + -- +   23   + -- +      |
          /      \      /      \      /      \
    |    +   42   + -- +   33   + -- +   24   +    |
          \      /      \      /      \      /
    |      + -- +   43   + -- +   34   + -- +      |
                 \      /      \      /
      --          + -- +   44   + -- +          --
          -             \      /             -
             --          + -- +          --
                 -                    -
                    --            --
                        -      -
                           --
    """

    @classmethod
    def get_valid_coordinates(cls, size):
        all_coordinates = [
            Coordinate(row, column)
            for row in range(size.height)
            for column in range(size.height)
        ]
        return [
            coordinate for
            coordinate in all_coordinates if
            abs(coordinate.row - coordinate.column) <= size.width // 2
        ]

    @classmethod
    def get_border_coordinates(cls, size):
        valid_coordinates = cls.get_valid_coordinates(size)
        return sorted(list({
            neighbor for
            coordinate in valid_coordinates for
            neighbor in coordinate.get_all_neighbors() if
            neighbor not in valid_coordinates
        }))

    def get_all_neighbors(self):
        return [
            Coordinate(self.row + i, self.column + j)
            for (i, j) in [
                (-1, -1), (-1,  0), ( 0, -1),
                ( 0,  1), ( 1,  0), ( 1,  1),
            ]
        ]

    def get_valid_neighbors(self, size):
        all_neighbors = self.get_all_neighbors()
        valid_coordinates = set(self.get_valid_coordinates(size))
        return [
            neighbor for
            neighbor in all_neighbors if
            neighbor in valid_coordinates
        ]
