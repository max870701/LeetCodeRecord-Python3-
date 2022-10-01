class MinStack(object):
    """
    Time complexity is O(1)
    Space complexity is O(N)
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or (self.min_stack[-1] >= val):
            self.min_stack.append(val)

    def push_improved(self, val):
        self.stack.append(val)

        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append([val, 1])

        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1
        
    def pop(self):
        """
        :rtype: None
        """
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def pop_improved(self, val):
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

    def getMin1(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()