class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.n = len(nums)
        self.res = []
        self.track = []
        self.used = [False] * self.n
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums):
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return

        for i in range(self.n):
            if self.used[i]:
                continue
            # 剪枝，固定相同的元素在排列中的相對位置
            if (i > 0) and (nums[i] == nums[i-1]) and (self.used[i-1] == False):
                # 若前面的相鄰香等元素沒有用過，則跳過;
                # 只有在前一個相對位置的元素已經使用過時，才會跳下一輪選擇
                # e.g. nums = [1, 2, 2', 2'']
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False