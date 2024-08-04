# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的二叉樹，判斷是否為高度差大於 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced
    
    # 給定 root 為根節點的二叉樹，返回最大高度
    def height(self, root):
        if not root: return 0
        if not self.balanced: return 0

        left_h = self.height(root.left)
        right_h = self.height(root.right)
        res = max(left_h, right_h)
        if abs(left_h - right_h) > 1:
            self.balanced = False
        
        return res + 1
    
class Solution1:
    def maxHeight(self, root) -> int:
        """
        Given a root node, return the maximum height of the tree
        """
        if root is None: return 0
        
        left_max = self.maxHeight(root.left)
        right_max = self.maxHeight(root.right)

        if abs(left_max - right_max) > 1:
            self.res = False

        return max(
            left_max,
            right_max
        ) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given root node, return if this tree is balanced.
        """
        self.res = True
        self.maxHeight(root)
        return self.res