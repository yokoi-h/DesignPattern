__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod
from Item import Item

class Link(Item):
    __metaclass__ = ABCMeta

    def __init__(self, caption, url):
        super(Link).__init__(caption)
        self.url = url



