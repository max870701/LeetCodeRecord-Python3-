# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 給定 root 為根節點的二叉樹，搜尋並返回以 val 為根節點的子樹
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # base case
        if root is None: return
        # 搜索值大於目前節點，搜索右子樹
        if val > root.val:
            return self.searchBST(root.right, val)
        # 搜索值小於目前節點，搜索左子樹
        if val < root.val:
            return self.searchBST(root.left, val)
        # 找到搜索值並返回該節點構成的BST
        return root