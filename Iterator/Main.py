__author__ = 'yokoi-h'

from BookShelf import BookShelf
from Book import Book

if __name__ == '__main__':
    bookShelf = BookShelf(4)
    bookShelf.append(Book("Around the World in 80 days"))
    bookShelf.append(Book("Bible"))
    bookShelf.append(Book("Cinderella"))
    bookShelf.append(Book("Daddy-Long-Legs"))
    it = bookShelf.iterator()

    while it.hasNext():
        book = it.next()
        print "book : ", book.getName()


