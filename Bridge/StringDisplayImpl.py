__author__ = 'yokoi-h'

from DisplayImpl import DisplayImpl

class StringDisplayImpl(DisplayImpl):

    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def rawOpen(self):
        self._printLine()

    def rawPrint(self):
        print "|%s|" % self.string

    def rawClose(self):
        self._printLine()

    def _printLine(self):
        line = '-' * self.width
        print '+%s+' % line




