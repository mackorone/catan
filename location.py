class Point(object):

    def __init__(self, row, column, corner):
        self.__row = row
        self.__column = column
        self.__corner = corner

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    @property
    def corner(self):
        return self.__corner
