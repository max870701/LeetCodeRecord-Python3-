# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.findSequence(root)
        return self.res
    
    # 輸入 root 為根節點的二叉樹，返回 (最長遞增序列長度, 最長地減序列長度)
    def findSequence(self, root):
        # Base case
        if root is None:
            return (0, 0)

        left = self.findSequence(root.left)
        right = self.findSequence(root.right)
        # 後序位置
        leftIncr, leftDecr = left
        rightIncr, rightDecr = right
        rootIncr, rootDecr = 1, 1
        
        if root.left:
            if root.left.val == root.val - 1:
                rootIncr += leftIncr
            elif root.left.val == root.val + 1:
                rootDecr += leftDecr

        if root.right:
            if root.right.val == root.val - 1:
                rootIncr = max(rootIncr, rightIncr + 1) # 對比左右
            elif root.right.val == root.val + 1:
                rootDecr = max(rootDecr, rightDecr + 1) # 對比左右

        self.res = max(self.res, rootIncr + rootDecr - 1)

        return (rootIncr, rootDecr)