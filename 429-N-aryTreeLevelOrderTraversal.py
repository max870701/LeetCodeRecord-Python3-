"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            level = []
            s = q.qsize()
            for _ in range(s):
                node = q.get()
                level.append(node.val)
                for child in node.children:
                    q.put(child)
            ans.append(level)
    
        return ansq