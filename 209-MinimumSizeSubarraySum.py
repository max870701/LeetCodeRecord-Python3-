class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        s = 0
        l = 0
        for r in range(len(nums)):
            s += nums[r]
            while s - nums[l] >= target:
                s -= nums[l]
                l += 1
            if s >= target:
                ans = min(ans, r - l + 1)
        return 0 if ans == float('inf') else ans