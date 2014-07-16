__author__ = 'yokoi-h'

import datetime, time

class Singleton(object):

    def __init__(self, name):
        self.name = name

t = datetime.datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
INSTANCE = Singleton(t)
