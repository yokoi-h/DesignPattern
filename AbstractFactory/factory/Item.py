__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Item(object):
    __metaclass__ = ABCMeta

    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def makeHTML(self):
        pass

