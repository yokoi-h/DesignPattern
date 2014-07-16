__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Factory(object):
    __metaclass__ = ABCMeta

    @staticmethod
    def getFactory(classname):
        """Loading function, class and module lazy."""
        try:
            mod = __import__(classname)
        except:
            mod_list = classname.split('.')
            mod = __import__('.'.join(mod_list[:-1]))

        components = classname.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        factory = mod
        return factory

    @abstractmethod
    def createLink(self, caption, url):
        pass

    @abstractmethod
    def createTray(self, caption):
        pass

    @abstractmethod
    def createPage(self, title, author):
        pass