__author__ = 'yokoi-h'

from Aggregate import Aggregate
from BookShelfIterator import BookShelfIterator

class BookShelfArray(Aggregate):

    def __init__(self, maxSize):
        super(BookShelfArray, self).__init__()
        self.__last = 0
        self.__books = []

    def getBookAt(self, index):
        return self.__books[index]

    def append(self, book):
        self.__books.append(book)
        self.__last += 1

    def getLength(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
