# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 1
        self.traverse(root, float('-inf'), 1)
        return self.maxLen

    def traverse(self, root, parentVal, l):
        if root is None: return

        if parentVal + 1 == root.val:
            l += 1
        else:
            l = 1
        
        self.maxLen = max(self.maxLen, l)
        self.traverse(root.left, root.val, l)
        self.traverse(root.right, root.val, l)