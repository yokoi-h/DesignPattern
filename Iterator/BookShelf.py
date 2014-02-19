__author__ = 'yokoi-h'

from Aggregate import Aggregate
from BookShelfIterator import BookShelfIterator

class BookShelf(Aggregate):

    def __init__(self, maxSize):
        super(BookShelf, self).__init__()
        self.__last = 0
        self.__books = [None] * maxSize

    def getBookAt(self, index):
        return self.__books[index]

    def append(self, book):
        self.__books[self.__last] = book
        self.__last += 1

    def getLength(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
