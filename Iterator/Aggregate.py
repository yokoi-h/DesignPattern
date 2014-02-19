__author__ = 'yokoi-h'

from abc import abstractmethod

class Aggregate(object):

    @abstractmethod
    def iterator(self):
        pass


