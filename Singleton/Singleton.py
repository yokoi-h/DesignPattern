__author__ = 'yokoi-h'

import datetime, time
from threading import BoundedSemaphore

semaphore = BoundedSemaphore(1)

class Singleton(object):

    __ins = None

    def __new__(cls, *args, **kwargs):
        semaphore.acquire()
        if cls.__ins is None:
            cls.__ins = super(Singleton, cls).__new__(cls, *args, **kwargs)
        semaphore.release()
        return cls.__ins


    def __init__(self, name):
        self.name = name

    @classmethod
    def getInstance(cls):
        return cls.__ins

print __name__
t = datetime.datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
Singleton(t)
