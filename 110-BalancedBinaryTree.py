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