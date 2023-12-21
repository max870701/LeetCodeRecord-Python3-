# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)
    
    def isValid(self, root, _min, _max):
        # base case
        if root is None: return True
        # 若 root 不符合 min 和 max 的限制，判斷為不合法
        if _min and (root.val <= _min.val): return False
        if _max and (root.val >= _max.val): return False
        # 限定左子樹的最大值是 root.val
        # 限定右子樹的最小值是 root.val
        return (self.isValid(root.left, _min, root)) and (self.isValid(root.right, root, _max))