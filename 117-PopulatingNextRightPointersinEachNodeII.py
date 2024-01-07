# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from queue import Queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            pre = Node(val=None)
            for _ in range(size):
                cur = q.get()
                if pre is not None:
                    pre.next = cur
                pre = cur
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
            
        return root