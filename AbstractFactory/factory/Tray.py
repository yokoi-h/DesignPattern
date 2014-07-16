__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod
from Item import Item

class Tray(Item):
    __metaclass__ = ABCMeta

    def __init__(self, caption):
        super(Tray).__init__(caption)
        self.tray = []

    def add(self, item):
        self.tray.append(item)




