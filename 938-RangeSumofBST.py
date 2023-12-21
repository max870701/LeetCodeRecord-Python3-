# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high 
        self.sum = 0
        self.traverseBST(root)
        return self.sum

    def traverseBST(self, root):
        if root is None: return

        if root.val >= self.low and root.val <= self.high:
            self.sum += root.val

        self.traverseBST(root.left)
        self.traverseBST(root.right)

        if root.left and root.left.val < self.low:
            root.left = None
        if root.right and root.right.val > self.high:
            root.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high 
        self.sum = 0
        self.traverseBST(root)
        return self.sum

    def traverseBST(self, root):
        if root is None: return
        # Out of the range
        if root.val < self.low: # 無需遍歷左子樹
            self.traverseBST(root.right)
        elif root.val > self.high: # 無需遍歷右子樹
            self.traverseBST(root.left)
        else: # In the range
            self.sum += root.val
            self.traverseBST(root.left)
            self.traverseBST(root.right)