# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.foundP, self.foundQ = False, False
        res = self.find(root, p.val, q.val)

        if not self.foundP or not self.foundQ:
            return None

        return res


    def find(self, root, val1, val2):
        if not root: return None

        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        # 後序位置
        # 判斷當前節點是否為 LCA
        if left is not None and right is not None:
            return root
        
        # 判斷當前節點是否為目標值
        if root.val == val1 or root.val == val2:
            if root.val == val1: self.foundP = True
            if root.val == val2: self.foundQ = True
            return root 
        
        return left if left else right