# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.path = ""
        self.res = None
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None: return
        # 葉子節點，更新路徑
        if root.left is None and root.right is None:
            self.path = chr(ord('a') + root.val) + self.path
            # Python中字符串比大小是由字典序
            if self.res is None or self.path < self.res:
                self.res = self.path[:]
            self.path = self.path[1:]
            return

        self.path = chr(ord('a') + root.val) + self.path
        self.traverse(root.left)
        self.traverse(root.right)
        self.path = self.path[1:]