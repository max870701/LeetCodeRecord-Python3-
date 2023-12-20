# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        self.s = 0
        self.left = False
        self.traverse(root)
        return self.s

    # 遍歷所有以 root 為根節點的二叉樹，並將所有左側葉子節點相加
    def traverse(self, root):
        if root is None:
            return
        if root.left is None and root.right is None and self.left:
            self.s += root.val
        self.left = True
        self.traverse(root.left)
        self.left = False
        self.traverse(root.right)