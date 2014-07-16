__author__ = 'yokoi-h'

from framework.Manager import Manager
from UnderlinePen import UnderlinePen
from MessageBox import MessageBox

if __name__ == "__main__":
    manager = Manager()

    upen = UnderlinePen("~")
    mbox1 = MessageBox("*")
    mbox2 = MessageBox("/")
    manager.register("strong message", upen)
    manager.register("warning box", mbox1)
    manager.register("slash box", mbox2)

    p1 = manager.create("strong message")
    p2 = manager.create("warning box")
    p3 = manager.create("slash box")
    p1.use("Hello World")
    p2.use("Hello World")
    p3.use("Hello World")



