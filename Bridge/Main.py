__author__ = 'yokoi-h'

from Display import Display
from CountDisplay import CountDisplay
from RandomDisplay import RandomDisplay
from StringDisplayImpl import StringDisplayImpl
from TextFileDisplayImpl import TextFileDisplayImpl

if __name__ == '__main__':

    d1 = Display(StringDisplayImpl("Hello Japan"))
    d2 = CountDisplay(StringDisplayImpl("Hello Japan"))
    d3 = CountDisplay(StringDisplayImpl("Hello Universe"))
    d4 = RandomDisplay(StringDisplayImpl("Hello Universe"))
    d5 = Display(TextFileDisplayImpl("test.txt"))
    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)
    d4.randomDisplay(5)
    d5.display()