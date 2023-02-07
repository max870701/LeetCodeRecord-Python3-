# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time Complexity: O(logN * logN)
        # In subtrees of a complete binary tree, at least one of them is a perfect binary tree.
        l, r = root, root
        # 沿最左側和最右側分別計算高度
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        # 如果左右側計算的高度相同，則是一棵滿二叉樹
        if hl == hr:
            return pow(2, hl) - 1
        # 如果左右高度不同，則按照普通二叉樹的邏輯計算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)