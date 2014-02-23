__author__ = 'yokoi-h'


from abc import abstractmethod

class Print(object):

    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printStrong(self):
        pass

