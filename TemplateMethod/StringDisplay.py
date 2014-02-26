__author__ = 'yokoi-h'

__author__ = 'yokoi-h'

from AbstractDisplay import AbstractDisplay

class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def open(self):
        self.printLine()

    def printString(self):
        print "|%s|" % self.string

    def close(self):
        self.printLine()

    def printLine(self):
        line = "-" * self.width
        print "+%s+" % line
