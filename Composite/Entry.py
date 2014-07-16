__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Entry(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    def addEntry(self, entry):
        raise FileTreatmentException()

    def printList(self):
        print ""

    @abstractmethod
    def printList(self, prefix):
        pass

    def toString(self):
        return self.getName() + "(" + self.getSize() +")"

