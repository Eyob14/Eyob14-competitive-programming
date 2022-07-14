class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue = []
        self.length = 0
        self.l = k

    def insertFront(self, value: int) -> bool:
        if self.length < self.l:
            self.dequeue.insert(0, value)
            self.length += 1
            if self.dequeue[0] == value:
                return True
            return False
    def insertLast(self, value: int) -> bool:
        if self.length < self.l:
            self.dequeue.append(value)
            self.length += 1
            if self.dequeue[-1] == value:
                return True
            return False
    def deleteFront(self) -> bool:
        if self.length != 0:
            self.dequeue.pop(0)
            self.length -= 1
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if self.length != 0:
            self.dequeue.pop()
            self.length -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.length:
            return self.dequeue[0]
        return -1
    def getRear(self) -> int:
        if self.length:
            return self.dequeue[-1]
        return -1
    def isEmpty(self) -> bool:
        if self.length:
            return False
        return True
    def isFull(self) -> bool:
        if self.length == self.l:
            return True
        return False