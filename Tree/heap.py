
class BinaryHeap(object):

    def __init__(self):

        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):

        while(i // 2 > 0):

            value = self.heapList[i]
            parent = self.heapList[i/2]
            if value < parent:
                self.heapList[i//2] = value
                self.heapList[i] = parent

            i = i // 2

    def insert(self, value):
        self.heapList.append(value)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)


    def minChild(self, i):

        left = 2 * i
        right = 2 * i + 1

        if right > self.currentSize:
            return left
        else:
            if self.heapList[left] < self.heapList[right]:
                return left
            else:
                return right

    def percDown(self, i):

        while i * 2 <= self.currentSize:
            mc = self.minChild(i)

            if self.heapList[mc] < self.heapList[i]:
                temp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = temp
            else:
                break

            i = mc


    def output(self):
        for value in enumerate(self.heapList):
            print(value)



bh = BinaryHeap()
bh.insert(9)
bh.insert(33)
bh.insert(5)
bh.insert(10)
bh.insert(1)
bh.insert(0)
bh.insert(17)
bh.insert(19)
bh.insert(22)
bh.insert(21)

bh.output()


