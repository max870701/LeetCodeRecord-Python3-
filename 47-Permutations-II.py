class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.track = []
        self.used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums):
        if len(self.track) == len(nums):
            self.res.append(list(self.track))
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
<<<<<<< HEAD
            # 剪枝，固定相同的元素在排列中的相對位置
            if (i > 0) and (nums[i] == nums[i-1]) and (not self.used[i-1]):
                # 若前面的相鄰香等元素沒有用過，則跳過;
                # 只有在前一個相對位置的元素已經使用過時，才會跳下一輪選擇
                # e.g. nums = [1, 2, 2', 2'']
=======
            if (i > 0) and (nums[i] == nums[i-1]) and (not self.used[i-1]):
>>>>>>> f9f54e79478cd19a53d73890894e947ebb05c3bd
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False