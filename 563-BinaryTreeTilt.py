# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.sumTree(root)
        return self.res
    
    # 輸入 root 為根節點的二叉樹，返回所有的元素和
    def sumTree(self, root):
        if root is None: return 0

        leftSum = self.sumTree(root.left)
        rightSum = self.sumTree(root.right)
        # 後序位置
        self.res += abs(rightSum - leftSum)

        return leftSum + rightSum + root.val