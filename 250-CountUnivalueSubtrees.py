# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = 0
        self.count(root)
        return self.ans
    
    # 給定 root 節點的二叉樹，若子樹節點都相同，則返回節點的值
    # [-1000, 1000]
    def count(self, root):
        left_v = root.val if not root.left else self.count(root.left)
        right_v = root.val if not root.right else self.count(root.right)
        if left_v == -1001 or right_v == -1001:
            return -1001
        if left_v == right_v and right_v == root.val:
            self.ans += 1
            return root.val
        
        return -1001