# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.getMinMax(root)
        return self.res

    # 給定 root 為根節點的二叉樹，返回二叉樹節點中的最大值和最小值，（最大值, 最小值）
    def getMinMax(self, root):
        if root is None:
            return (float('-inf'), float('inf'))
        
        left_max, left_min = self.getMinMax(root.left)
        right_max, right_min = self.getMinMax(root.right)
        # 後序位置
        root_max = max(left_max, right_max, root.val)
        root_min = min(left_min, right_min, root.val)
        # 更新 res 值，計算最大差值
        self.res = max(self.res, root_max - root.val , root.val - root_min)

        return (root_max, root_min)