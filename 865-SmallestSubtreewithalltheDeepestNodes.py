# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 求最深節點的最近公共祖先(LCA)
        res = self.maxDepth(root)
        return res[1]

    # 給定 root 為根節點的二叉樹，返回最大深度以及最深夜子節點的公共祖先
    def maxDepth(self, root: TreeNode) -> (int, TreeNode):
        # Base case
        if root is None:
            return (0, None)
        
        left_max, left_lca = self.maxDepth(root.left)
        right_max, right_lca = self.maxDepth(root.right)
        # 後序位置
        # (1) 若左右子樹一樣深，則當前節點為LCA
        if left_max == right_max:
            return (left_max + 1, root)
        # (2) 若左右子樹不一樣深，那麼最深葉子節點的LCA在深度較深的那邊
        res = (left_max + 1, left_lca) if left_max > right_max else (right_max + 1, right_lca)
        return res