__author__ = 'yokoi-h'

import sys
from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print "<<",

    def printString(self):
        sys.stdout.write(self.ch)

    def close(self):
        print ">>"

