__author__ = 'yokoi-h'

from FactoryMethod.framework.Factory import Factory
from IDCard import IDCard
from threading import BoundedSemaphore

class IDCardFactory(Factory):

    def __init__(self):
        self.owner = []
        self.seqNum = 1
        self.semaphore = BoundedSemaphore(1)

    def createProduct(self, owner):
        self.semaphore.acquire()
        card = IDCard(self.seqNum, owner)
        self.seqNum += 1
        self.semaphore.release()
        return card

    def registerProduct(self, product):
        self.owner.append(product.getOwner())

    def getOwners(self):
        return self.owner

