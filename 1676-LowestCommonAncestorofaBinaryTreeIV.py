# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        val_set = set()
        for node in nodes:
            val_set.add(node.val)
        
        return self.find(root, val_set)
    
    # 給定 root 為根節點的二叉樹，返回 val_set 中所有值的最近公共祖先節點
    def find(self, root, val_set):
        if not root: return None
        # 前序位置
        if root.val in val_set:
            return root
        left = self.find(root.left, val_set)
        right = self.find(root.right, val_set)
        # 後序位置
        if left is not None and right is not None:
            return root

        return left if left else right