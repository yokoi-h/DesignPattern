__author__ = 'yokoi-h'

from abc import ABCMeta, abstractmethod

class Sorter(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, data):
        pass


class SelectionSorter(Sorter):

    def sort(self, data):
        for i in range(0, len(data)):
            min = i
            for j in range(i + 1, len(data)):
                if data[min] > data[j]:
                    min = j
            passingplace = data[min]
            data[min] = data[i]
            data[i] = passingplace


class HeapSorter(Sorter):

    def sort(self, data):
        heap = []
        index = 0
        for d in data:
            heap.append(d)
            self.recover(heap)
            index += 1

        for i in range(len(heap) - 1, -1, -1):
            data[i] = heap.pop(0)
            self.recover(heap)

    def recover(self, heap):

        if len(heap) <= 1:
            return

        for i in range(len(heap) - 1, 0, -1):
            parent = (i - 1) / 2
            if heap[parent] < heap[i]:
                temp = heap[i]
                heap[i] = heap[parent]
                heap[parent] = temp


class SortAndPrint(object):

    def __init__(self, data, sorter):
        self.data = data
        self.sorter = sorter

    def execute(self):
        self.printData()
        self.sorter.sort(self.data)
        self.printData()

    def printData(self):
        datastr = ""
        for d in self.data:
            datastr += "%s," % d
        print datastr


if __name__ == "__main__":
    data = ["Dumpty", "Bowman","Carroll","Elfland","Alice"]
    sorter = SortAndPrint(data,SelectionSorter())
    sorter.execute()

    #data = ["Dumpty", "Bowman","Carroll","Elfland","Alice"]
    data = [5, 1, 3, 6, 7, 8, 9, 0, 2, 4]
    sorter = SortAndPrint(data,HeapSorter())
    sorter.execute()
