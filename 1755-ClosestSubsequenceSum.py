# 雙向 BFS
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        # 剪枝：常數時間優化
        maxVal, minVal = 0, 0
        for num in nums:
            if num >= 0:
                maxVal += num
            else:
                minVal += num
        if goal > maxVal: return goal - maxVal
        if goal < minVal: return minVal - goal
        # 排序: 用於 collect() 剪枝
        nums.sort()
        lsum, rsum = [], []

        self.size = 0
        self.collect(nums, 0, n >> 1, 0, lsum)
        lsize = self.size

        self.size = 0
        self.collect(nums, n >> 1, n, 0, rsum)
        rsize = self.size

        lsum.sort()
        rsum.sort()
        # 雙指針
        ans = abs(goal)
        right = rsize - 1
        for left in range(lsize):
            while right > 0 and abs(goal - lsum[left] - rsum[right-1]) <= abs(goal - lsum[left] - rsum[right]):
                right -= 1
            ans = min(ans, abs(goal-lsum[left]-rsum[right]))

        return ans


    def collect(self, nums, start, end, sum_val, sum_arr):
        if start == end:
            sum_arr.append(sum_val)
            self.size += 1
        else:
            j = start + 1
            while j < end and nums[j] == nums[j-1]:
                j += 1
            range_size = j - start
            # [1 1 1 1 1 2]
            #  i         j
            for k in range(range_size + 1):
                self.collect(nums, j, end, k * nums[start] + sum_val, sum_arr)