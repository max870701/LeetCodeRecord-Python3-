# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 記錄結果
        self.res = 0
        # 記錄當前元素排名
        self.rank = 0
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root is None:
            return
        self.traverse(root.left, k)
        # 中序遍歷，為升序 root.left < root < root.right
        # 最小值為最左下角的節點
        self.rank += 1
        if self.rank == k:
            # 找到第k小的元素
            self.res = root.val
            return
        #######################
        self.traverse(root.right, k)