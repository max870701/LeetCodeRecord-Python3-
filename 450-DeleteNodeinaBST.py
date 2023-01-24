# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMin(self, node):
        # 最左元素為最小值
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # base case
        if root is None:
            return None
        if root.val == key:
            # 清況一 + 情況二
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 情況三
            # 獲取右子樹最小節點
            minNode = self.getMin(root.right)
            # 用右子樹最小節點替換 root 節點
            root.right = self.deleteNode(root.right, minNode.val)
            # 構造以 minNode 做為根節點的樹
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root