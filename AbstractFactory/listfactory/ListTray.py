__author__ = 'yokoi-h'

from ..factory.Tray import Tray

class ListTray(Tray):

    def __init__(self, caption):
        super(ListTray, self).__init__(caption)

    def makeHTML(self):
        s = "<li>\n"
        s = s + self.caption + "\n"
        s += "<ul>\n"
        for i in self.tray:
            s += i.makeHTML()

        s += "</ul>\n"
        s += "</li>\n"

        return s

