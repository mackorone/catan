""" Represents a board coordinate, e.g.,

                + -- + 
               /      \ 
         + -- +   00   + -- +
        /      \      /      \ 
  -    +   10   + -- +   01   +    -
        \      /      \      /       
-   20   + -- +   11   + -- +   02   -
        /      \      /      \       
  -    +   21   + -- +   12   +    -
        \      /      \      /       
         + -- +   22   + -- +         
               \      /              
                + -- +              

"""
from collections import namedtuple


Coordinate = namedtuple('Coordinate', ['row', 'column'])
