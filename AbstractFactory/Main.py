__author__ = 'yokoi-h'

from factory.Factory import Factory
from factory.Item import Item
from factory.Link import Link
from factory.Page import Page
from factory.Tray import Tray
import sys

if __name__ == "__main__":
    classname = sys.argv[1]

    factory = Factory.getFactory(classname)
    asahi = factory.createLink("Asahi", "http://www.asahi.com")
    yomiuri = factory.createLink("Yomiuri", "http://www.yomiuri.co.jp")
    yahoo = factory.createLink("Yahoo", "http://www.yahoo.com")
    yahooJP = factory.createLink("Yahoo", "http://www.yahoo.co.jp")
    google = factory.createLink("Yahoo", "http://www.google.com")
    excite = factory.createLink("Yahoo", "http://www.excite.co.jp")

    traynews = factory.createTray("Newspaper")
    traynews.add(asahi)
    traynews.add(yomiuri)

    trayyahoo = factory.createTray("Yahoo")
    trayyahoo.add(yahoo)
    trayyahoo.add(yahooJP)

    traysearch = factory.createTray("Search Engine")
    traysearch.add(trayyahoo)
    traysearch.add(google)
    traysearch.add(excite)

    page = factory.createPage("Link Page", "Hiroshi Yuki")
    page.add(traynews)
    page.add(traysearch)












