__author__ = 'yokoi-h'

class Player(object):

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.wincount = 0
        self.losecount = 0
        self.gamecount = 0

    def nextHand(self):
        return self.strategy.nextHand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def __repr__(self):
        return '[%s:%s games, %s win, %s lose]' % (self.name, self.gamecount, self.wincount, self.losecount)
