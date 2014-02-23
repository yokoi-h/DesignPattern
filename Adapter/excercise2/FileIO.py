__author__ = 'yokoi-h'

from abc import abstractmethod
import ConfigParser

class FileIO(object):

    def readFromFile(self, string):
        pass

    def writeToFile(self, string):
        pass

    def setValue(self, key, value):
        pass

    def getValue(self, key):
        pass


class FileProperties(FileIO):

    Section = "general"

    def readFromFile(self, string):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(string)

    def getValue(self, key):
        value = self.parser.get(self.Section, key)
        return value

    def setValue(self, key, value):
        self.parser.set(self.Section, key, value)

    def writeToFile(self, string):
        print "subclass"
        cfgfile = open(string, 'w')
        self.parser.write(cfgfile)


