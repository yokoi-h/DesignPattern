__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Builder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def makeTitle(self, title):
        pass

    @abstractmethod
    def makeString(self, str):
        pass

    @abstractmethod
    def makeItems(self, items):
        pass

    @abstractmethod
    def close(self):
        pass