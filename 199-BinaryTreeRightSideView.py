# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return None
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                node = q.get()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    q.put(node.right)
                if node.left:
                    q.put(node.left)
        
        return res