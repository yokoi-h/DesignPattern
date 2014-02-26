__author__ = 'yokoi-h'

from FactoryMethod.framework.Product import Product

class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner
        print "Create %s's card." % self.owner

    def use(self):
        print "Use %s's card." % self.owner

    def getOwner(self):
        return self.owner

