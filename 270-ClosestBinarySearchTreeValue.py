# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = float('inf')
        self.traverse(root, target)
        return self.ans

    # 遍歷以 root 為根節點的 BST，搜尋距離 target 最近的答案，如果有多個答案，則返回較小的
    def traverse(self, root, target):
        if root is None: return

        if target < root.val:
            self.traverse(root.left, target)
            # 中序位置
            if abs(root.val - target) < abs(self.ans - target):
                self.ans = root.val
        else: # target >= root.val
            # 中序位置
            if abs(root.val - target) < abs(self.ans - target):
                self.ans = root.val
            self.traverse(root.right, target)