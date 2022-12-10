# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # Record subTree
        self.memo = defaultdict(int)
        # Record duplicated root
        self.res = []
        self.traverse(root)
        return self.res
    

    def traverse(self, root):
        if root is None:
            return "#"
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        #postorder traverse
        #postorder build subTree
        subTree = str(left) + "," + str(right) + "," + str(root.val)
        # You can also use preorder build subTree
        # subTree = str(root.val) + "," + str(left) + "," + str(right)

        freq = self.memo[subTree]
        if freq == 1:
            self.res.append(root)
        self.memo[subTree] += 1
        return subTree
