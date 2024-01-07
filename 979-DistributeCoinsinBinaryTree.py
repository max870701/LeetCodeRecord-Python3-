# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.getCoinsNeed(root)
        return self.res

    # 給定 root 為根節點的二叉樹，返回多的硬幣數量(+為多 -為少)  
    def getCoinsNeed(self, root) -> int:
        if root is None: return 0
        left_need = self.getCoinsNeed(root.left)
        right_need = self.getCoinsNeed(root.right)

        self.res += abs(left_need) + abs(right_need) + (root.val - 1)

        return left_need + right_need + (root.val - 1)