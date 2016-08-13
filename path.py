from abc import (
    ABCMeta,
    abstractmethod,
)


class Path(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass
