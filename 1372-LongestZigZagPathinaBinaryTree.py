# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.getPathLen(root)
        return self.res

    # 給定 root 為根節點的二叉樹，返回 (從root向左走的最長交錯路徑長度, 從root向右走的最長交錯路徑長度)
    def getPathLen(self, root):
        if root is None:
            return (-1, -1)

        left_left, left_right = self.getPathLen(root.left)
        right_left, right_right = self.getPathLen(root.right)
        # 後序
        root_left = left_right + 1
        root_right = right_left + 1

        self.res = max(self.res, root_left, root_right)

        return (root_left, root_right)