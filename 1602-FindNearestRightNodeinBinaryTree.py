# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if u is None: return None
        q = Queue()
        q.put(root)
        while not q.empty():
            sz = q.qsize()
            found = False
            for _ in range(sz):
                cur_node = q.get()
                if found:
                    return cur_node
                if cur_node.val == u.val:
                    found = True

                if cur_node.left: q.put(cur_node.left)
                if cur_node.right: q.put(cur_node.right)

        return None