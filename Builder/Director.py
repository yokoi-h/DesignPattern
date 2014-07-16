__author__ = 'yokoi-h'

class Director(object):

    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        self.__builder.makeTitle("Greeting")
        self.__builder.makeString("from this morning to afternoon")
        self.__builder.makeItems(["Good morning", "Hello"])
        self.__builder.makeString("in the evening")
        self.__builder.makeItems(["Good evening", "Good night", "Good bye"])
        self.__builder.close()

