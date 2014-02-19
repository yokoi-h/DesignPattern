__author__ = 'yokoi-h'

from Iterator import Iterator

class BookShelfIterator(Iterator):

    def __init__(self, bookShelf):
        self.bookShelf = bookShelf
        self.index = 0

    def hasNext(self):
        bookShelf = self.bookShelf
        if (self.index < bookShelf.getLength()):
            return True
        else:
            return False

    def next(self):
        bookShelf = self.bookShelf
        book = bookShelf.getBookAt(self.index)
        self.index += 1
        return book

