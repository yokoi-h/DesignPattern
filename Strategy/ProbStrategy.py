__author__ = 'yokoi-h'

from Strategy import Strategy
import random
from Hand import Hand

class ProbStrategy(Strategy):

    def __init__(self, seed):
        self.prevHandValue = 0
        self.currentHandValue = 0

        self.history = [[1,1,1],
                   [1,1,1],
                   [1,1,1]]

        self.r = random
        self.r.seed(seed)

    def nextHand(self):
        bet = self.r.randint(0,self.getSum(self.currentHandValue))
        handValue = 0
        if(bet < self.history[self.currentHandValue][0]):
            handValue = 0
        elif (bet < self.history[self.currentHandValue][0] +
            self.history[self.currentHandValue][1]):
            handValue = 1
        else:
            handValue = 2

        self.prevHandValue = self.currentHandValue
        self.currentHandValue = handValue
        return Hand.getHand(handValue)

    def getSum(self, hv):
        sum = 0
        for i in range(0, 2):
            sum += self.history[hv][i]

        return sum

    def study(self, win):
        if win:
            self.history[self.prevHandValue][self.currentHandValue] += 1
        else:
            self.history[self.prevHandValue][(self.currentHandValue + 1) % 3] += 1
            self.history[self.prevHandValue][(self.currentHandValue + 2) % 3] += 1

