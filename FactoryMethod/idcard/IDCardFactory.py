__author__ = 'yokoi-h'

from FactoryMethod.framework.Factory import Factory
from IDCard import IDCard

class IDCardFactory(Factory):

    def __init__(self):
        self.owner = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.owner.append(product.getOwner())

    def getOwners(self):
        return self.owner

