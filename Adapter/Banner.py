__author__ = 'yokoi-h'


class Banner(object):

    def __init__(self, string):
        self.string = string

    def showWithParen(self):
        print "(%s)\n"% self.string,

    def showWithAster(self):
        print "*%s*\n"% self.string,


