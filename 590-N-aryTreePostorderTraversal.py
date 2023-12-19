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

    def postorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.arr
        
    # 遍歷以 root 為根節點的多叉樹
    def traverse(self, root):
        if root is None: return
        for child_node in root.children:
            self.traverse(child_node)
        self.arr.append(root.val)