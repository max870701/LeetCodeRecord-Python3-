# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.traverse(root)
        return root
    
    def traverse(self, root):
        if root is None:
            return
        # 降序
        self.traverse(root.right)
        # 中序位置
        self.sum += root.val
        root.val = self.sum
        ###############
        self.traverse(root.left)