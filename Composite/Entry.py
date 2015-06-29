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

    @abstractmethod
    def getAbsolutePath(self):
        pass

    def addEntry(self, entry):
        raise FileTreatmentException

    def printList(self):
        self._printList()

    @abstractmethod
    def _printList(self, prefix=''):
        pass

    def __str__(self):
        return '%s (%d)' % (self.getName(), self.getSize())


class FileTreatmentException(Exception):
    def printException(self):
        print 'FileTreatmentException'


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.path = ''

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def _printList(self, prefix=''):
        print '%s/%s' % (prefix, self)

    def getAbsolutePath(self):
        return self.path + "/" + self.name


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []
        self.path = '/' + name

    def getName(self):
        return self.name

    def getAbsolutePath(self):
        return self.path + "/" + self.name

    def getSize(self):
        size = 0
        for d in self.directory:
            size += d.getSize()

        return size

    def add(self, entry):
        entry.path = self.name
        self.directory.append(entry)
        return self

    def _printList(self, prefix=''):

        print("absolute path: "+self.getAbsolutePath())

        print(prefix + "/" + str(self))
        for e in self.directory:
            e._printList(prefix + '/' + self.name)




