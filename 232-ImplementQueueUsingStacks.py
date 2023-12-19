class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)
        self.inToOut()

    def pop(self) -> int:
        self.inToOut()
        return self.outStack.pop()

    def peek(self) -> int:
        self.inToOut()
        return self.outStack[-1]

    def empty(self) -> bool:
        return (not self.inStack) and (not self.outStack)
    
    # 倒數據
    # inStack -> outStack
    # 1) 只有在 outStack 為空時才倒
    # 2) 若倒數據，需一次倒完 inStack 所有元素
    def inToOut(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()