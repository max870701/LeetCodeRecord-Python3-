# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的二叉樹和 target 值，返回刪除所有葉子節點值為 target 的二叉樹
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None: return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # Post Order ：已知左右子樹的情況後，判斷自身是否符合刪除條件才進行刪除
        # 刪除條件: 1)該節點為葉子節點 2)節點的值等於 target 值
        if root.left is None and root.right is None and root.val == target:
            return None
        
        return root