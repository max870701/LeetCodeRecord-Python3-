# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    # 函數傳入 root 為根節點的二叉樹，返回前序遍歷的 list
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        self.arr.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.arr