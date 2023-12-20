# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        minLevel = None
        level = 1
        q = Queue()
        q.put(root)

        while not q.empty():
            levelSum = 0
            s = q.qsize()
            for _ in range(s):
                node = q.get()
                levelSum += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = level
            level += 1

        return minLevel