# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        self.getCountAndSum(root)
        return self.res

    # 給定 root 為根節點的二叉樹，返回節點總數和節點之和
    def getCountAndSum(self, root) -> (int, int):
        if root is None:
            return (0, 0)
        left_cnt, left_sum = self.getCountAndSum(root.left)
        right_cnt, right_sum = self.getCountAndSum(root.right)
        # 後序位置
        root_cnt = left_cnt + right_cnt + 1
        root_sum = left_sum + right_sum + root.val
        # 更新 res 值
        self.res = max(self.res, root_sum / root_cnt)

        return (root_cnt, root_sum)