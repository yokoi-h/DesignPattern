__author__ = 'yokoi-h'

from abc import abstractmethod

class Iterator(object):

    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass
