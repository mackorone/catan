from resource import Resource


class Tile(object):

    def __init__(self, resource, number):
        assert isinstance(resource, Resource)
        assert number in list(range(2, 12 + 1))
        self.resource = resource
        self.number = number

    def __str__(self):
        template = [
           '  0 -- 0  ',
           ' / rrrr \ ',
           '0 r ## r 0',
           ' \ rrrr / ',
           '  0 -- 0  ',
        ]
        string = '\n'.join(template)
        # string = string.replace('0', ' ')
        string = string.replace('r', self.resource.char)
        string = string.replace('##', str(self.number).zfill(2))
        return string

# TODO: Describe the sideways row/col
'''
         0 -- 0 
        / rrrr \ 
  0 -- 0 r ## r 0 -- 0
 / rrrr \ rrrr / rrrr \ 
0 r ## r 0 -- 0 r ## r 0
 \ rrrr / rrrr \ rrrr /
  0 -- 0 r ## r 0 -- 0
 / rrrr \ rrrr / rrrr \ 
0 r ## r 0 -- 0 r ## r 0
 \ rrrr / rrrr \ rrrr /
  0 -- 0 r ## r 0 -- 0
        \ rrrr /
         0 -- 0 
'''
