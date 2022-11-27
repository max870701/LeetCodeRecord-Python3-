# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return
        
        root.left, root.right = root.right, root.left

        self.traverse(root.left)
        self.traverse(root.right)

        
class Solution1(object):
    # 定義：將以root為根的這顆二叉樹翻轉，返回翻轉後的二叉樹的根節點
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # 利用函數定義，先翻轉左右子樹
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # 交換左右子節點
        root.left, root.right = right, left
        # 和定義邏輯自洽：以root為根的這顆二叉樹已經被反轉，返回root
        return root