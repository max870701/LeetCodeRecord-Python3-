# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build(nums, 0, len(nums)-1)

    def build(self, nums, lo, hi):
        """
        定義： 將 nums[lo..hi] 機造成符合條件的樹，返回根節點
        """
        # base case
        if lo > hi:
            return None

        index = -1
        max_value = -sys.maxint - 1

        # 找最大值和紀錄index
        for i in range(lo, hi+1):
            if nums[i] > max_value:
                index = i
                max_value = nums[i]
        # 構建以 max value 為根節點的樹
        root = TreeNode(val=max_value)
        # 遞歸調用來構建左右子樹
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)

        return root