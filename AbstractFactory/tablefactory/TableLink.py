__author__ = 'yokoi-h'

from ..factory.Link import Link

class TableLink(Link):

    def __init__(self, caption, url):
        super(TableLink, self).__init__(caption, url)

    def makeHTML(self):
        s = "<td><a href=\""+self.url+"\">"+self.caption+"/a></td>"
        return s



