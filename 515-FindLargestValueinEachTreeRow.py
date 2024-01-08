# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return None
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            size = q.qsize()
            levelMax = float('-inf')
            for _ in range(size):
                cur_node = q.get()
                levelMax = max(levelMax, cur_node.val)
                if cur_node.left:
                    q.put(cur_node.left)
                if cur_node.right:
                    q.put(cur_node.right)

            ans.append(levelMax)
        
        return ans