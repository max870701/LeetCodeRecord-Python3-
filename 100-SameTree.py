# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定以 p 和 q 為根節點的兩顆二叉樹，判斷是否相同。 分解問題：p, q左右子樹是否相同
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 到葉子節點皆相同
        if p is None and q is None: return True
        # 其中一個為None，則必不相同
        if not p or not q: return False
        # 節點值不相同
        if p.val != q.val: return False
        
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))

class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given p, q two root node, return if they are the same tree.
        """
        # Base case
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        # The same tree condition 1: p.val == q.val
        if p.val != q.val:
            return False
        
        # The same tree condition 2: (p.left and q.left is the same tree) and (p.right and q.right is the same tree)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)