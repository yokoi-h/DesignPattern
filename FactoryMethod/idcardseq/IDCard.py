__author__ = 'yokoi-h'

from FactoryMethod.framework.Product import Product

class IDCard(Product):

    def __init__(self, seqNum, owner):
        self.owner = owner
        self.seqNum = seqNum
        print "Create {0}'s card({1})...".format(self.owner, self.seqNum)

    def use(self):
        print "Use %s's card." % self.owner

    def getOwner(self):
        return self.owner

