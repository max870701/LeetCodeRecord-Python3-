"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.arr = []

    def preorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.arr
        
    # 遍歷多叉樹
    def traverse(self, root):
        if root is None: return
        self.arr.append(root.val)
        for child_node in root.children:
            self.traverse(child_node)