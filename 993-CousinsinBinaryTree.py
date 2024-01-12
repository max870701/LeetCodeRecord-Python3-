# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x, self.y = x, y
        self.depthX, self.depthY = 0, 0
        self.parentX, self.parentY = None, None
        self.traverse(root, None, 0)
        if self.depthX == self.depthY and self.parentX != self.parentY:
            return True
        return False

    def traverse(self, root, parent, depth):
        if root is None: return

        if root.val == self.x:
            self.depthX = depth
            self.parentX = parent
        if root.val == self.y:
            self.depthY = depth
            self.parentY = parent

        self.traverse(root.left, root, depth + 1)
        self.traverse(root.right, root, depth + 1)