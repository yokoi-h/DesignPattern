__author__ = 'yokoi-h'

from Banner import Banner
from Print import Print

class PrintBanner(Banner, Print):

    def __init__(self, string):
        super(PrintBanner, self).__init__(string)

    def printWeak(self):
        self.showWithParen()

    def printStrng(self):
        self.showWithAster()


class PrintBanner2(Print):

    def __init__(self, string):
        super(PrintBanner2, self).__init__()
        self.banner = Banner(string)


    def printWeak(self):
        self.banner.showWithParen()
        print "PrintBanner2"

    def printStrng(self):
        self.banner.showWithAster()
        print "PrintBanner2"