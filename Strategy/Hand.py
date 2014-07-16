__author__ = 'yokoi-h'


class Hand(object):

    HANDVALUE_G = 0
    HANDVALUE_C = 1
    HANDVALUE_P = 2
    hand = []
    hand_name = ['Gu', 'Choki', 'Pa']

    def __init__(self, handValue):
        self.handValue = handValue

    @classmethod
    def getHand(cls, handValue):
        ret = cls.hand[handValue]
        return ret

    def isStrongerThan(self, hand):
        return self.fight(hand) == 1

    def isWeakerThan(self, hand):
        return self.fight(hand) == -1

    def fight(self, hand):
        if(hand == self):
            return 0
        elif((self.handValue + 1) == hand.handValue):
            return 1
        else:
            return -1

    def toString(self):
        return self.hand_name[self.handValue]

Hand.hand = [Hand(Hand.HANDVALUE_G),
             Hand(Hand.HANDVALUE_C),
             Hand(Hand.HANDVALUE_P)]