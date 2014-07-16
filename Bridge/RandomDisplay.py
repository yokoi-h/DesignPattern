__author__ = 'yokoi-h'

from Display import Display
import random

class RandomDisplay(Display):

    def __init__(self, impl):
        super(RandomDisplay, self).__init__(impl)

    def randomDisplay(self, times):
        self.open()
        t = random.randint(0, times)
        for i in range(t):
            self.print_body()

        self.close()