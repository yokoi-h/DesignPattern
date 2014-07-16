__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Product(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def createClone(self):
        pass

