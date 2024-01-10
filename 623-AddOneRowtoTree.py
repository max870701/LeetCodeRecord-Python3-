# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root, right=None)
        self.target_depth = depth
        self.target_val = val
        self.level = 0
        self.traverse(root)
        return root
    
    def traverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return

        self.level += 1
        if self.level == self.target_depth - 1:
            new_left, new_right = TreeNode(val=self.target_val), TreeNode(val=self.target_val)
            new_left.left, new_right.right = root.left, root.right
            root.left, root.right = new_left, new_right

        self.traverse(root.left)
        self.traverse(root.right)
        self.level -= 1