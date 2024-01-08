# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    # 給定 root 為根節點的二叉樹，判斷是否為完全二叉樹
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        q.put(root)
        truncated = False
        while not q.empty():
            sz = q.qsize()
            for _ in range(sz):
                cur_node = q.get()
                if cur_node is None:
                    if not truncated:
                        truncated = True
                else:
                    if truncated:
                        return False          
                    q.put(cur_node.left)
                    q.put(cur_node.right)
                
        return True