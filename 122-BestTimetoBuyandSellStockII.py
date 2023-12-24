class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp_table = [[0 for _ in range(2)] for _ in range(days)]

        for d in range(days):
            if d == 0:
                dp_table[0][0] = 0
                dp_table[0][1] = -prices[d]
                continue

            dp_table[d][0] = max(dp_table[d-1][0], dp_table[d-1][1] + prices[d])
            dp_table[d][1] = max(dp_table[d-1][1], dp_table[d-1][0] - prices[d])

        return dp_table[days-1][0]
    
# 優化空間複雜度
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')

        for d in range(days):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[d])
            dp_i_1 = max(dp_i_1, tmp - prices[d])

        return dp_i_0
    