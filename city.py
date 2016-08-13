from building import Building


class City(Building):

    @property
    def multiplier(self):
        return 2
