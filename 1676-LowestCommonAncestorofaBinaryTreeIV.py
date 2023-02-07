# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, values):
        if root is None: return None
        # 前序
        if root.val in values:
            return root
        #
        left = self.find(root.left, values)
        right = self.find(root.right, values)
        # 後序
        if left and right:
            return root
        #
        return left if left is not None else right
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        values = set()
        for node in nodes:
            values.add(node.val)
        return self.find(root, values)