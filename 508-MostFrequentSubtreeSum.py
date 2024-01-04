# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # 遍歷二叉樹統計出現頻率
        self.sum_cnt = defaultdict(int)
        self.sumTree(root)
        # 找到出現次數頻率最高的子樹和
        maxCnt = 0
        for v in self.sum_cnt.values():
            maxCnt = max(maxCnt, v)
        # 找到 maxCnt 對應的子樹和
        ans = []
        for k in self.sum_cnt.keys():
            if self.sum_cnt[k] == maxCnt:
                ans.append(k)
            
        return ans



    def sumTree(self, root):
        if root is None: return 0

        left = self.sumTree(root.left)
        right = self.sumTree(root.right)
        s = left + right + root.val
        # 後序
        self.sum_cnt[s] += 1
        return s