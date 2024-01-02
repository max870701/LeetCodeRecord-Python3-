# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p.val, q.val)

    # 給定 root 為根節點的二叉樹，返回存在 val1, val2 的最近公共祖先節點
    def find(self, root, val1, val2):
        if root is None: return None
        # 前序位置
        if root.val == val1 or root.val == val2: # 遇到目標值直接返回
            return root
        # 左右子樹查找
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        # 後序位置
        if left is not None and right is not None:
            return root
        
        return left if left else right