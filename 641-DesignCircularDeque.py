class MyCircularDeque:

    def __init__(self, k: int):
        self.r = 0
        self.l = 0
        self.size = 0
        self.dq = [0] * k
        self.limit = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            # 被刪光後的 dequeue 需要重置 self.r 和 self.l 位置，並在 0 位置上加入新值
            self.r = self.l = 0
            self.dq[0] = value
        else:
            self.l = self.limit - 1 if self.l == 0 else self.l - 1
            self.dq[self.l] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.r = self.l = 0
            self.dq[0] = value
        else:
            self.r = 0 if self.r == self.limit - 1 else self.r + 1
            self.dq[self.r] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.l = 0 if self.l == self.limit - 1 else self.l + 1
        self.size -= 1
        return True  

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.r = self.limit - 1 if self.r == 0 else self.r - 1
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.l]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.r]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()