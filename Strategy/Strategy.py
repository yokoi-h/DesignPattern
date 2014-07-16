__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Strategy(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass

