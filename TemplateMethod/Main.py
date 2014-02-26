__author__ = 'yokoi-h'

from AbstractDisplay import AbstractDisplay
from CharDisplay import CharDisplay
from StringDisplay import StringDisplay

if __name__ == '__main__':
    d1 = CharDisplay("H")
    d1.display()

    d2 = StringDisplay("Hello")
    d2.display()

    d3 = StringDisplay("See You")
    d3.display()

