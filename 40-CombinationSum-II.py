class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == 0:
            return []
        # Sorting 
        candidates.sort()
        # Initialize varialbes
        self.res = []
        self.track = []
        self.tracksum = 0
        self.backtrack(candidates, 0, target)
        return self.res

    def backtrack(self, nums, start, target):
        # base case, 達到目標和, 找到符合條件的組合
        if self.tracksum == target:
            self.res.append(list(self.track))
            return
        # base case, 超過目標和, 結束
        if self.tracksum > target:
            return
        # backtracking framework
        for i in range(start, len(nums)):
            # 剪枝
            if i > start and nums[i] == nums[i-1]:
                continue
            # 做選擇
            self.track.append(nums[i])
            self.tracksum += nums[i]
            # 遞歸遍歷
            self.backtrack(nums, i+1, target)
            # 撤銷選擇
            self.track.pop()
            self.tracksum -= nums[i]


class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.trackSum = 0
        self.track = []
        l = len(candidates)
        self.backtrack(candidates, 0, l, target)
        return self.ans

    def backtrack(self, nums, start, end, target):
        if start > end: return
        # Base case
        if self.trackSum == target:
            self.ans.append(self.track[:])
            return
        if self.trackSum > target:
            return
        for i in range(start, end):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.track.append(nums[i])
            self.trackSum += nums[i]
            self.backtrack(nums, i+1, end, target)
            self.track.pop()
            self.trackSum -= nums[i]