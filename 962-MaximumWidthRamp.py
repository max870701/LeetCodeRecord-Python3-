class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 0 索引位置必壓入棧
        mono_stack = [0]
        n = len(nums)
        r = 1
        max_ramp = 0
        # 由左向右遍歷
        for i in range(n):
            # 嚴格遞減壓入棧
            if nums[i] < nums[mono_stack[r-1]]:
                mono_stack.append(i)
                r += 1
        # 由右向左遍歷
        for j in range(n-1, -1, -1):
            while r > 0 and nums[j] >= nums[mono_stack[r-1]]:
                cur = mono_stack.pop()
                r -= 1
                max_ramp = max(max_ramp, j - cur)

        return max_ramp