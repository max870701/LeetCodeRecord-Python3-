# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None: return

        if not root.left and root.right:
            self.res.append(root.right.val)
        if not root.right and root.left:
            self.res.append(root.left.val)

        self.traverse(root.left)
        self.traverse(root.right)