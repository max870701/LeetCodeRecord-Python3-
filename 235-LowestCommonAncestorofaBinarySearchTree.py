# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, val1, val2):
        if root is None: return None
        # 當前節點太小，去右子樹找
        if root.val < val1:
            return self.find(root.right, val1, val2)
        # 當前節點太大，去左子樹找
        if root.val > val2:
            return self.find(root.left, val1, val2)
        # val1 <= root.val <= val2，則當前節點為 LAC
        return root

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)