__author__ = 'yokoi-h'

from ..factory.Page import Page

class ListPage(Page):

    def __init__(self, title, author):
        super(ListPage, self).__init__(title, author)

    def makeHTML(self):
        s = "<html><head><title>%s</title></head>\n" % self.title
        s += "<body>\n"
        s += "<h1>%s</h1>\n" % self.title
        s += "<ul>\n"
        for i in self.content:
            s += i.makeHTML()

        s += "</ul>\n"
        s += "<hr><address>%s</address>\n" % self.author
        s += "</body></html>\n"

        return s

