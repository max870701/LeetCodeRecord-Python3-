class MyCircularQueue:

    def __init__(self, k: int):
        self.l = 0
        self.r = 0
        self.size = 0
        self.limit = k
        self.arr = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.arr[self.r] = value
        self.r = 0 if self.r == self.limit - 1 else self.r + 1
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.arr[self.l] = 0
        self.l = 0 if self.l == self.limit - 1 else self.l + 1
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.l]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.r - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()