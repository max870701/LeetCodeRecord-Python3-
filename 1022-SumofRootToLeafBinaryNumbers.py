# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.n = 0
        self.res = 0
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None: return

        if root.left is None and root.right is None:
            self.res += (self.n << 1) | root.val
            return

        self.n = (self.n << 1) | root.val
        self.traverse(root.left)
        self.traverse(root.right)
        self.n = self.n >> 1