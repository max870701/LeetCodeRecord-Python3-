# 非遞歸實現
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Order:
    def __init__(self):
        self.stack = []

    # preOrder 壓棧順序: 中, 右, 左 
    def preOrder(self, head):
        if head:
            self.stack.append(head)
            while self.stack:
                node = self.stack.pop()
                print(node.val)
                print(',')
                if node.right: self.stack.append(node.right)
                if node.left: self.stack.append(node.left)
    # inOrder 壓棧順序：左, 中, 右
    def inOrder(self, head):
        if head:
            while head or self.stack:
                # 壓入所有 node.left
                if head:
                    self.stack.append(head)
                    head = head.left
                else:
                    head = self.stack.pop()
                    print(head.val)
                    head = head.right
    # postOrder 壓棧順序：左, 右, 中 -> 為 preOrder': 中, 右, 左 的逆序
    def postOrder(self, head):
        self.collect = []
        self.stack.append(head)
        while self.stack:
            head = self.stack.pop()
            self.collect.append(head)
            if head.left: self.stack.append(head.left)
            if head.right: self.stack.append(head.right)
        while self.collect:
            print(self.collect.pop().val)