# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.leaves = []
        self.traverse(root, 0)
        self.leaves.sort(key=lambda x: x[1], reverse=True)
        return self.leaves[0][0]

    def traverse(self, root, depth):
        if root is None: return
        if root.left is None and root.right is None:
            self.leaves.append((root.val, depth))

        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)