__author__ = 'yokoi-h'

from abc import abstractmethod
from Product import Product

class Factory(object):

    def create(self, owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

    @abstractmethod
    def createProduct(self, owner):
        pass

    @abstractmethod
    def registerProduct(self, product):
        pass