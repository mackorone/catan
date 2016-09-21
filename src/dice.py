from collections import (
    defaultdict,
    namedtuple,
)
from itertools import combinations
from random import random


Die = namedtuple('Die', ['sides'])


class Dice(object):

    DICE = [
        Die(sides=6),
        Die(sides=6),
    ]

    @staticmethod
    def possibilities():
        min_value = len(Dice.DICE)
        max_value = sum(die.sides for die in Dice.DICE)
        return list(range(min_value, max_value + 1))

    @staticmethod
    def probabilities():
        # TODO: upforgrabs
        raise NotImplementedError

    @staticmethod
    def roll():
        return sum(
            1 + int(die.sides * random())
            for die in Dice.DICE
        )

    @staticmethod
    def roll_n_times(n):
        counts = defaultdict(int)
        for roll in range(n):
            counts[Dice.roll()] += 1
        return dict(counts)
