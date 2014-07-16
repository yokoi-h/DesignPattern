__author__ = 'yokoi-h'

from ..factory.Page import Page

class TablePage(Page):

    def __init__(self, title, author):
        super(TablePage, self).__init__(title, author)

    def makeHTML(self):
        s = "<html><head><title>%s</title></head>\n" % self.title
        s += "<body>\n"
        s += "<table> width=\"80\" border=\"3\">"
        s += "<tr>\n"
        for i in self.content:
            s += i.makeHTML()

        s += "</tr>\n"
        s += "</table>\n" % self.author
        s += "<hr><address>%s</address>\n" % self.author
        s += "</body></html>\n"

        return s
