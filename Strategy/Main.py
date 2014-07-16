__author__ = 'yokoi-h'

import sys

from Player import Player
from WiningStrategy import WinningStrategy
from ProbStrategy import ProbStrategy
from RandomStrategy import RandomStrategy


if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print "argument is not correct"
        exit()

    seed1 = sys.argv[1]
    seed2 = sys.argv[2]

    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", RandomStrategy(seed2))

    for i in range(0, 10000):
        nextHand1 = player1.nextHand()
        nextHand2 = player2.nextHand()
        if(nextHand1.isStrongerThan(nextHand2)):
            print "Winner:%s" % player1
            player1.win()
            player2.lose()

        elif (nextHand2.isStrongerThan(nextHand1)):
            print "Winner:%s" % player2
            player2.win()
            player1.lose()
        else:
            print "Even ..."
            player2.even()
            player1.even()

    print "Total result:"
    print player1
    print player2

