# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.res = 0
        self.maxLen(root, root.val)
        return self.res

    # 計算以 root 為根節點的二叉樹中，從root開始值為parentVal的最大長度(邊)
    def maxLen(self, root, parentVal) -> int:
        if root is None: return 0

        left_max = self.maxLen(root.left, root.val)
        right_max = self.maxLen(root.right, root.val)
        # 後序位置更新最大長度
        self.res = max(self.res, left_max + right_max)
        # 若 root.val 不是 parentVal 返回 0 (斷掉)
        if root.val != parentVal:
            return 0
        
        return 1 + max(left_max, right_max)