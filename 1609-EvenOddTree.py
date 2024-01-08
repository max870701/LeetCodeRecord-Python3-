# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        q.put(root)
        level = 0
        while not q.empty():
            sz = q.qsize()
            prev = None
            for _ in range(sz):
                node = q.get()
                if level % 2 == 0: # 偶數層
                    # 條件：奇數、嚴格遞增
                    if node.val % 2 == 0 or (prev and node.val <= prev.val):
                        return False
                else: # 奇數層
                    # 條件：偶數、嚴格遞減
                    if node.val % 2 == 1 or (prev and node.val >= prev.val):
                        return False
                prev = node

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            level += 1
        
        return True