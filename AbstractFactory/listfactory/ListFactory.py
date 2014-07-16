__author__ = 'yokoi-h'

from ..factory.Factory import Factory

class ListFactory(Factory):

    def createLink(self, caption, url):
        return ListLink(url)

    def createPage(self, title, author):
        return ListPage(title, author)

    def createTray(self, caption):
        return ListTray(caption)

