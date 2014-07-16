__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class DisplayImpl(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def rawOpen(self):
        pass

    @abstractmethod
    def rawPrint(self):
        pass

    @abstractmethod
    def rawClose(self):
        pass

