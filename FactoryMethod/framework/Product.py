__author__ = 'yokoi-h'

from abc import abstractmethod

class Product(object):

    @abstractmethod
    def use(self):
        pass

