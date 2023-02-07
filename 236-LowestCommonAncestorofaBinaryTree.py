# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, val1, val2):
        if root is None: return None
        # 前序
        if root.val == val1 or root.val == val2:
            return root
        #
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        # 後序
        if left is not None and right is not None:
            return root
        #
        return left if left is not None else right
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.find(root, p.val, q.val)