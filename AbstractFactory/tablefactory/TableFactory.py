__author__ = 'yokoi-h'

from ..factory.Factory import Factory

class TableFactory(Factory):

    def createLink(self, caption, url):
        return TableLink(caption, url)

    def createTray(self, caption):
        return TableTray(caption)

    def createPage(self, title, author):
        return TablePage(title, author)

