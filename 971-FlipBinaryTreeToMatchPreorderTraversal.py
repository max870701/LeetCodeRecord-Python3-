# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        # 前序遍歷的順序
        self.voyage = voyage
        self.index = 0
        # 記錄翻轉的節點
        self.res = []
        # Flag
        self.canFlip = True
        self.traverse(root)
        if self.canFlip:
            return self.res
        return [-1]

    def traverse(self, root):
        if root is None or not self.canFlip:
            return

        if root.val != self.voyage[self.index]:
            self.canFlip = False
            return

        self.index += 1
        if root.left is not None and root.left.val != self.voyage[self.index]:
            root.left, root.right = root.right, root.left
            self.res.append(root.val)
        
        self.traverse(root.left)
        self.traverse(root.right)