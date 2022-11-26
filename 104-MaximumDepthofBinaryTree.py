# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 定義：輸入根節點，返回這顆樹的最大深度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else: 
            # 分別計算左右子樹的最大深度
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            # 取左右子樹中的最大值，再加上跟節點本身
            return max(leftHeight, rightHeight) + 1