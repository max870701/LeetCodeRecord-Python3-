class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # base case
        if candidates == 0:
            return []
        self.res = []
        self.track = []
        self.tracksum = 0
        self.backtrack(candidates, 0, target)
        return self.res

    def backtrack(self, nums, start, target):
        # base case, 找到目標，紀錄結果
        if self.tracksum == target:
            self.res.append(list(self.track))
            return
        # base case, 超過目標和，停止向下遍歷
        if self.tracksum > target:
            return
        # backtracking frame
        for i in range(start, len(nums)):
            # select
            self.tracksum += nums[i]
            self.track.append(nums[i])
            # next level
            self.backtrack(nums, i, target)
            # withdraw select
            self.tracksum -= nums[i]
            self.track.pop()


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.n = len(candidates)
        self.ans = []
        self.track = []
        self.target = target
        self.curSum = 0
        self.backtrack(candidates, 0)
        return self.ans

    def backtrack(self, nums, start):
        if self.curSum == self.target:
            self.ans.append(self.track[:])
            return
        
        if self.curSum > self.target:
            return

        for i in range(start, self.n):
            self.track.append(nums[i])
            self.curSum += nums[i]
            self.backtrack(nums, i)
            self.track.pop()
            self.curSum -= nums[i]