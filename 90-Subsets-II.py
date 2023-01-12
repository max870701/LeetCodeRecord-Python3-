class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        self.track = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, start):
        # 前序位置，每個節點都是子集
        self.res.append(list(self.track))
        
        for i in range(start, len(nums)):
            # 剪枝邏輯，值相同的相鄰樹枝，只遍歷一次
            if (i > start) and (nums[i] == nums[i-1]):
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i+1)
            self.track.pop()
        