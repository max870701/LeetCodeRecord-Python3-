# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Queue import Queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        q = Queue()
        q.put(root)
        depth = 1

        while not q.empty():
            sz = q.qsize()
            for _ in range(sz):
                cur = q.get()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
            depth += 1
        return depth
                