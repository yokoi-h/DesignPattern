__author__ = 'yokoi-h'

from Display import Display

class CountDisplay(Display):

    def __init__(self, impl):
        super(CountDisplay, self).__init__(impl)

    def multiDisplay(self, times):
        self.open()
        for i in range(times):
            self.print_body()

        self.close()

