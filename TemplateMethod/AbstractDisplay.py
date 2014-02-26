__author__ = 'yokoi-h'


from abc import abstractmethod

class AbstractDisplay(object):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def printString(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(0,5):
            self.printString()
        self.close()

