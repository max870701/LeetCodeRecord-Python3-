# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的二叉樹，刪除子樹和小於limit值的節點，並返回刪除後的樹
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None: return None
        # 前序：葉子節點
        if root.left is None and root.right is None:
            if root.val < limit:
                return None
            return root

        left = self.sufficientSubset(root.left, limit - root.val)
        right = self.sufficientSubset(root.right, limit - root.val)
        # 後序：左右子樹皆被刪除，即不滿足 limit - root.val 條件，那麼經過 root 則不滿足 limit
        if left is None and right is None:
            return None
        
        root.left, root.right = left, right
        return root