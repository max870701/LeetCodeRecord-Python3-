# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 計算直徑即為計算某個節點的左右子樹最大深度之和（不包含節點本身）
        self.maxDiameter = 0
        self.maxDepth(root)
        return self.maxDiameter
    
    # 給定 root 為根節點的二叉樹，返回最大深度
    def maxDepth(self, root):
        if root is None: return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        # 後序位置
        d = left_max + right_max
        self.maxDiameter = max(self.maxDiameter, d)

        return max(left_max, right_max) + 1