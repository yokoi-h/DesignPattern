__author__ = 'yokoi-h'

from Strategy import Strategy
from Hand import Hand
import random

class RandomStrategy(Strategy):

    def __init__(self, seed):
        self.random = random
        self.random.seed(seed)

    def nextHand(self):
        hand = Hand.getHand(self.random.randint(0, 2))
        return hand

    def study(self, win):
        pass

