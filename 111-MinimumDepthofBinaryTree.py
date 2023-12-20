# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution(object):
    # 廣度優先的解法
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
                # 第一個到的葉子節點即為最小深度的節點
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
            depth += 1
        return depth


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.ans = float('inf')
        self.d = 0
        self.traverse(root)
        return self.ans

    # 遍歷一遍以 root 為根節點的二叉樹，到達根節點後更新最小深度
    def traverse(self, root):
        if root is None:
            return
        self.d += 1
        if root.left is None and root.right is None:
            self.ans = min(self.ans, self.d)
        self.traverse(root.left)
        self.traverse(root.right)
        self.d -= 1
                