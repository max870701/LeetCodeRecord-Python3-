# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.memo = dict()
    # 給定 root 為根節點的二叉樹，返回最大收益
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root in self.memo:
            return self.memo[root]
        # 搶，再去下下層搶
        do_rob = root.val + \
                (self.rob(root.left.left) + self.rob(root.left.right) if root.left else 0) + \
                (self.rob(root.right.left) + self.rob(root.right.right) if root.right else 0)
        # 不搶，去搶下層
        not_do_rob = self.rob(root.left) + self.rob(root.right)

        res = max(do_rob, not_do_rob)
        self.memo.setdefault(root, res)
        return res

class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dp(root)
        return max(res[0], res[1])

    # 給定 root 為根節點的二叉樹，返回長度為2的 tuple
    # tuple[0] 為不搶 root 所獲得的最大金額
    # tuple[1] 為搶 root 所獲得的最大金額
    def dp(self, root):
        if root is None: return (0, 0)
        left = self.dp(root.left)
        right = self.dp(root.right)
        # 搶這層，下層不能搶
        rob_root = root.val + left[0] + right[0]
        # 不搶這層，下層可搶可不搶(取決於收益)
        not_rob_root = max(left[0], left[1]) + max(right[0], right[1])
        return (not_rob_root, rob_root)