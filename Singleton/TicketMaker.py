__author__ = 'yokoi-h'

from threading import BoundedSemaphore

semaphore = BoundedSemaphore(1)

class TicketMaker(object):

    __ins = None

    def __new__(cls, *args, **kwargs):
        if cls.__ins is None:
            ins = super(TicketMaker, cls).__new__(cls,  *args, **kwargs)
            cls.__ins = ins
        return cls.__ins

    def __init__(self):
        self.ticket = 1000

    @classmethod
    def getInstance(cls):
        return cls.__ins

    def getNextTicketNumber(self):
        semaphore.acquire()
        self.__ins.ticket += 1
        num = self.__ins.ticket
        semaphore.release()
        return num

TicketMaker()
