# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.num = 0
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return
        # 前序
        self.num = self.num * 10 + root.val
        if root.left is None and root.right is None:
            self.res += self.num
        self.traverse(root.left)
        self.traverse(root.right)
        # 後序
        self.num //= 10