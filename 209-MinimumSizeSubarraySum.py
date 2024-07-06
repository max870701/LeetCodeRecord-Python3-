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


class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n)
        # 滑動窗口最小長度
        # 窗口擴張和縮小的條件
        left = 0
        right = 0
        n = len(nums)
        ans = float('inf')
        tmp = 0
        # 窗口滑動條件
        while right < n:
            # 擴大窗口
            tmp += nums[right]
            right += 1
            # 縮小窗口
            while tmp - nums[left] >= target:
                tmp -= nums[left]
                left += 1
            
            # 題目要求大於等於 target 的最小子串長度
            if tmp >= target:
                ans = min(ans, right - left)
        
        return 0 if ans == float('inf') else ans