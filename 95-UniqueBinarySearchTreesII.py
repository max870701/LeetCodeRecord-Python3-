# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #base case
        if n == 0:
            return []
        return self.build(1, n)

    def build(self, lo, hi):
        # 構造閉區間 [lo, hi] 的 TreeList
        res = []
        # base case
        if lo > hi:
            res.append(None)
            return res
        # 窮舉 root 節點的所有可能
        for i in range(lo, hi+1):
            # 遞歸結構造出左右子BST的列表
            leftTree = self.build(lo, i-1)
            rightTree = self.build(i+1, hi)
            # 給 root 窮舉所有左右子樹的組合
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
