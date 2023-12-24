class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp_table = [[0 for _ in range(2)] for _ in range(days)]

        for d in range(days):
            # Base case
            # 第一天
            if d == 0:
                dp_table[0][0] = 0
                dp_table[0][1] = -prices[0]
            # 第二天
            elif d == 1:
                dp_table[1][0] = max(dp_table[0][0], dp_table[0][1] + prices[1])
                dp_table[1][1] = max(dp_table[0][1], dp_table[0][0] - prices[1])
            # 狀態轉移方程
            else:
                dp_table[d][0] = max(dp_table[d-1][0], dp_table[d-1][1] + prices[d])
                dp_table[d][1] = max(dp_table[d-1][1], dp_table[d-2][0] - prices[d])

        return dp_table[days-1][0]
    

# 空間複雜度優化
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        # dp[-1][0], dp[-1][1], dp[-2][0]
        dp_i_0, dp_i_1, dp_pre_0 = 0, float('-inf'), 0

        for d in range(days):
            # 狀態轉移方程
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[d])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[d])
            dp_pre_0 = tmp

        return dp_i_0