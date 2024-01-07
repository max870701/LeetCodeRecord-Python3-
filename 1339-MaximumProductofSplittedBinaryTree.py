# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 先遍歷一次二叉樹得到總和
        self.treeSum = self.getTreeSum(root)
        # 計算
        self.res = 0
        self.getSum(root)
        return self.res % 1000000007

    # 給定 root 為根節點的二叉樹，返回所有節點的和
    def getTreeSum(self, root) -> int:
        if root is None: return 0
        left_sum = self.getTreeSum(root.left)
        right_sum = self.getTreeSum(root.right)
        # 後序
        return left_sum + right_sum + root.val

    # 給定 root 為根節點的二叉樹，計算最大乘積，並返回所有節點的和
    def getSum(self, root) -> int:
        if root is None: return 0
        left_sum = self.getSum(root.left)
        right_sum = self.getSum(root.right)
        # 後序
        root_sum = left_sum + right_sum + root.val
        self.res = max(self.res, (root_sum * (self.treeSum - root_sum)))
        return root_sum