from path import Path


class Road(Path):

    @property
    def permanent(self):
        return True
