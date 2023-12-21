# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root1 和 root2 為根節點的兩顆二叉樹，返回合併後的二叉樹 (e.g. root2 接到 root1)
    # 1) 若 root1 為空，則接上 root2
    # 2) 若 root2 為空，則接上 root1
    # 3) 若 root1, root2 皆有值，則將兩個節點值進行相加
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: return root2
        if root2 is None: return root1
        
        root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        # root1.val = root1.val + root2.val

        return root1