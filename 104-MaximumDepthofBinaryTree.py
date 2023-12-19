# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 遍歷二叉樹的思路
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 記錄最大深度
        self.res = 0
        # 記錄遍歷到的節點的深度
        self.depth = 0 
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            # 到達葉子節點時，更新最大深度
            self.res = max(self.res, self.depth)
            return
        # Pre-order, 進入節點前
        self.depth += 1
        # 
        self.traverse(root.left)
        self.traverse(root.right)
        # Post-order, 維護self.depth
        self.depth -= 1
        
    # 分解問題的思路
    # 定義：輸入根節點，返回這顆樹的最大深度
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
       
        # 分別計算左右子樹的最大深度
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        # 取左右子樹中的最大值，再加上跟節點本身
        return max(leftHeight, rightHeight) + 1