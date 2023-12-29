# 自頂向下
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        self.memo = [-1] * self.n
        return self.dp(0)

    # 返回 nums[start:] 能搶到的最大值
    def dp(self, start):
        if start >= self.n: return 0
        if self.memo[start] != -1: return self.memo[start]
        res = max(
            # 不搶
            self.dp(start+1),
            # 搶
            self.nums[start] + self.dp(start+2)
        )
        self.memo[start] = res
        return res
    
# 自底向上
class Solution2:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.dp()

    # 迭代所有結果
    def dp(self):
        # 從第 i 間房子開始搶的最大金額
        # base case: 第 n 間開始搶為 0 
        dp_table = [0] * (self.n + 2)
        for i in range(self.n-1, -1, -1):
            dp_table[i] = max(
                # 搶: 金額等於這間的金額 + 下下間開始搶的金額
                dp_table[i+2] + self.nums[i],
                # 不搶: 金額等於從下一間開始搶
                dp_table[i+1]
            )
        return dp_table[0]
    
# 自底向上(空間優化)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.dp()

    # 迭代所有結果
    def dp(self):
        # 從第 i 間房子開始搶的最大金額
        # base case
        # dp[i+1], dp[i+2]
        dp_i_1, dp_i_2 = 0, 0
        # dp[i]
        dp_i = 0
        for i in range(self.n-1, -1, -1):
            dp_i = max(
                dp_i_2 + self.nums[i],
                dp_i_1
            )
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            
        return dp_i