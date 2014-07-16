__author__ = 'yokoi-h'

from framework.Product import Product
import copy

class MessageBox(Product):

    def __init__(self, decochar):
        self.__decochar = decochar

    def use(self, s):
        length = len(s)
        line = self.__decochar * (length + 4)

        print "%s" % line
        print "%s %s %s" % (self.__decochar, s, self.__decochar)
        print "%s" % line

    def createClone(self):
        clone = copy.deepcopy(self)
        return clone
