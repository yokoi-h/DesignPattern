__author__ = 'yokoi-h'

from Singleton import Singleton
from Singleton2 import INSTANCE

if __name__ == "__main__":
    ins1 = Singleton.getInstance()
    ins2 = Singleton.getInstance()
    print ins1.name
    print ins2.name
    if ins1 is ins2:
        print "same"
    else:
        print "different"

    ins3 = Singleton("hoge")
    if ins1 is ins3:
        print "same"
    else:
        print "different"

    ins4 = INSTANCE
    ins5 = INSTANCE
    print ins4.name
    print ins5.name
    if ins4 is ins5:
        print "same"
    else:
        print "different"
