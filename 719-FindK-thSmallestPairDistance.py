class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # the range of diff is [0, max - min]
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        ans = 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            if self.f(nums, mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    # 給定距離，返回符合條件的pair數量
    def f(self, nums, distance):
        n = len(nums)
        count = 0
        r = 0
        for l in range(n):
            while (r + 1 < n and nums[r+1] - nums[l] <= distance):
                r += 1
            count += r - l
        return count