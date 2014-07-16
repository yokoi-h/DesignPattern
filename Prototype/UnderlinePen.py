__author__ = 'yokoi-h'

from framework.Product import Product
import copy

class UnderlinePen(Product):

    def __init__(self, ulchar):
        self.__ulchar = ulchar

    def use(self, s):
        length = len(s)
        line = self.__ulchar * (length + 2)

        print "\"%s\"" % s
        print "%s" % line

    def createClone(self):
        clone = copy.deepcopy(self)
        return clone
