__author__ = 'yokoi-h'

from ..factory.Link import Link

class ListLink(Link):

    def __init__(self, caption, url):
        super(ListLink, self).__init__(caption, url)

    def makeHTML(self):
        s = " <li><a href=\"%s\">%s</a></li>" % (self.caption, self.url)
        return s


