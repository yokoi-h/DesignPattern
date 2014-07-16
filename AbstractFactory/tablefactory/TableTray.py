__author__ = 'yokoi-h'

from ..factory.Tray import Tray

class TableTray(Tray):

    def __init__(self, caption):
        super(TableTray, self).__init__(caption)

    def makeHTML(self):
        s = "<td>"
        s += "<table width=\"100\" border=\"1\"><tr>"
        s += "<td bgcolor=\"#cccccc\" align=\"center\" colspan=\""+len(self.tray)+"\"><b>"+self.caption+"</b></td>"
        s += "</tr>"
        s += "<tr>"
        for item in self.tray:
            s += item.makeHTML()
        s += "</tr></table>"
        s += "</td>"
        return s
