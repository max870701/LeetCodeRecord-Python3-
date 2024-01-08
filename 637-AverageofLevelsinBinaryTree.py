# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            sz = q.qsize()
            levelSum = 0
            for _ in range(sz):
                cur_node = q.get()
                levelSum += cur_node.val
                if cur_node.left:
                    q.put(cur_node.left)
                if cur_node.right:
                    q.put(cur_node.right)
            
            ans.append(levelSum / sz)
        
        return ans