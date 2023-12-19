# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    # 遍歷 root 為根節點的二叉樹，並原地翻轉 left, right nodes
    def traverse(self, root):
        # Base case
        if root is None:
            return
        # 翻轉
        root.left, root.right = root.right, root.left
        # 遍歷左右子樹
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
    

class Solution2:
    # 定義：對 root 為根節點的二叉樹的 left, right node 進行翻轉，返回翻轉後的左右子樹
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if root is None: return
        # 左右翻轉
        root.left, root.right = root.right, root.left
        # 遍歷左右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
