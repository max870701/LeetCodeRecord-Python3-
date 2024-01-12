# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        self.traverse(root, root.val)
        return self.cnt

    def traverse(self, root, pathMax):
        if root is None: return

        if pathMax <= root.val:
            self.cnt += 1

        pathMax = max(pathMax, root.val)
        self.traverse(root.left, pathMax)
        self.traverse(root.right, pathMax)