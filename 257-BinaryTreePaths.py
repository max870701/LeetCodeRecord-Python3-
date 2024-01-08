# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.path = []
        self.traverse(root)
        return self.ans

    def traverse(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.path.append(root.val)
            self.ans.append("->".join(map(str, self.path)))
            self.path.pop()
            return

        self.path.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        self.path.pop()