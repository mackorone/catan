# TODO: MACK - dedup with point

class Edge(object):

    def __init__(self, row, column, side):
        self.__row = row
        self.__column = column
        self.__side = side

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    @property
    def side(self):
        return self.__corner
