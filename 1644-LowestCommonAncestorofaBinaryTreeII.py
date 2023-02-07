# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, val1, val2):
        if root is None: return None
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        # 後序
        # 判斷 LAC node
        if left and right:
            return root
        # 判斷當前節點是否為目標值
        if root.val == val1 or root.val == val2:
            if root.val == val1:
                self.foundP = True
            if root.val == val2:
                self.foundQ = True
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
        self.foundP, self.foundQ = False, False
        res = self.find(root, p.val, q.val)
        if not self.foundP or not self.foundQ:
            return None
        return res