# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        while not q.empty():
            sz = q.qsize()
            levelSum = 0
            for _ in range(sz):
                node = q.get()
                levelSum += node.val
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
        
        return levelSum