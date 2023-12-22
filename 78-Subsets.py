class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.track = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        # 前序位置，每個節點的值都是一個子集
        self.res.append(list(self.track))
        # 回溯算法框架
        for i in range(start, len(nums)):
            # 做選擇
            self.track.append(nums[i])
            # 通過 start 參數控制樹枝的遍歷，避免產生重複的子集
            self.backtrack(nums, i+1)
            # 撤銷選擇
            self.track.pop()


class Solution2:
    def __init__(self):
        self.ans = []
        self.track = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums)
        return self.ans
    
    def backtrack(self, nums):
        self.ans.append(self.track[:])
        for i in range(len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums[i+1:])
            self.track.pop()