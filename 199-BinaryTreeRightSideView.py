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

class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        res = []
        q = Queue()
        q.put(root)

        while not q.empty():
            cur_qsize = q.qsize()
            right_node = None

            for _ in range(cur_qsize):
                cur_node = q.get()

                if cur_node:
                    right_node = cur_node

                if cur_node.left:
                    q.put(cur_node.left)
                
                if cur_node.right:
                    q.put(cur_node.right)

            res.append(right_node.val)
        
        return res