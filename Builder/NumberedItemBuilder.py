__author__ = 'yokoi-h'

from Builder import Builder

class NumberedItemBuilder(Builder):

    def __init__(self):
        self.buffer = []

    def makeTitle(self, title):
        self.buffer.append("======================\n")
        self.buffer.append(title+"\n")
        self.buffer.append("\n")

    def makeString(self, str):
        self.buffer.append("-"+str+"\n")

    def makeItems(self, items):
        itemNum = 1
        for i in items:
            self.buffer.append("("+str(itemNum)+")"+i+"\n")
            itemNum += 1

    def close(self):
        self.buffer.append("======================\n")

    def getResult(self):
        output = ""
        for item in self.buffer:
            output += item

        return output



