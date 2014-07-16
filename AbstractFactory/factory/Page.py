__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Page(object):
    __metaclass__ = ABCMeta


    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def output(self):
        filename = self.title + ".html"
        f = open(filename, "w")
        f.write(self.makeHTML())
        f.close()
        print filename + " was created."

    @abstractmethod
    def makeHTML(self):
        pass

