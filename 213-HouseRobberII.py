class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        if self.n == 1: return nums[0]
        return max(
            self.robRange(0, self.n-2), # 首搶尾不搶
            self.robRange(1, self.n-1)  # 首不搶尾搶
        )
    
    def robRange(self, start, end):
        # Base case
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(end, start-1, -1):
            dp_i = max(
                dp_i_2 + self.nums[i],
                dp_i_1
            )
            dp_i_1, dp_i_2 = dp_i, dp_i_1
        return dp_i