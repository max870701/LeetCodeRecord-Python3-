# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的 BST，將不在 [low, high] 範圍中的節點刪除，並返回刪除後的BST
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None: return None

        if root.val < low: # 左側直接不用看了，返回右側刪除後的子樹
            return self.trimBST(root.right, low, high)
        if root.val > high: # 右側直接不用看了，返回左側刪除後的子樹
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root