from pieces import (
    HEXAGONS,
    NUMBERS,
)
from random import shuffle
from resource import Resource
from tile import Tile
from tile_graphic import (
    TILE_GRID,
    TileGraphic,
    grid_to_str,
)

# TODO: MACK - this should encompass all graphics


class BoardGraphic(object):

    def __init__(self, board):
        self._board = board

    def __str__(self, fancy=True):

        # TODO: MACK- return a grid, convert to string
        
        # TODO: MACK - put all hardcoded logic in one place

        tile_height = len(TILE_GRID)
        tile_narrow = len(''.join(TILE_GRID[0]).strip())
        tile_wide = len(''.join(TILE_GRID[len(TILE_GRID) // 2]).strip())

        total_height = (tile_height - 1) * self._board.height + 1
        total_width = (
            (self._board.width // 2 + 1) * (tile_wide   - 1) +
            (self._board.width // 2    ) * (tile_narrow - 1) + 1
        )
        grid = [
            [' ' for i in range(total_width)]
            for j in range(total_height)
        ]

        for i, row in enumerate(self._board._board):
            for j, tile in enumerate(row):

                # TODO: MACK - Clean this logic up
                if i <= self._board.width // 2:
                    spaces_from_top = (i + j) * (tile_height // 2)
                else:
                    spaces_from_top = (
                        ((self._board.width // 2 + j) * (tile_height // 2)) +
                        ((i - (self._board.width // 2)) * (tile_height - 1))
                    )

                if i < self._board.width // 2:
                    spaces_from_left = (
                        ((self._board.width // 2) - i + j) *
                        ((tile_wide + tile_narrow) // 2 - 1)
                    )
                else:
                    spaces_from_left = (
                        j * ((tile_wide + tile_narrow) // 2 - 1)
                    )

                for tile_i, tile_line in enumerate(TileGraphic(tile).grid(fancy=fancy)):
                    for tile_j, char in enumerate(tile_line):
                        if char != ' ':
                            grid[spaces_from_top + tile_i][spaces_from_left + tile_j] = char
                    
        return grid_to_str(grid)

# TODO: Describe the sideways row/col
'''

                   + -- + 
                  /      \ 
            + -- +   00   + -- +
           /      \      /      \ 
     + -- +   10   + -- +   01   + -- +
    /      \      /      \      /      \
   +   20   + -- +   11   + -- +   02   +
    \      /      \      /      \      /
     + -- +   21   + -- +   12   + -- +
    /      \      /      \      /      \
   +   30   + -- +   22   + -- +   13   +
    \      /      \      /      \      /
     + -- +   31   + -- +   23   + -- +
    /      \      /      \      /      \
   +   40   + -- +   32   + -- +   24   +
  / \      /      \      /      \      /
 2=--+ -- +   41   + -- +   33   + -- +
           \      /      \      /
            + -- +   42   + -- +
                  \      / \
                   + -- +--2:
                    \  /
                     3?

'''
