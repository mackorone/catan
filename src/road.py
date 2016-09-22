class Road():

    def __init__(self, player):
        self.__player = player

    @property
    def player(self):
        return self.__player
