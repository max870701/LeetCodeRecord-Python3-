class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max_k = 2
        dp_table = [[[0] * 2 for _ in range(max_k+1)] for _ in range(days)]

        for d in range(days):
            # 盡量嘗試達成最大交易次數
            for k in range(max_k, 0, -1):
                # 第一天
                if d == 0:
                    dp_table[0][k][0] = 0
                    dp_table[0][k][1] = -prices[d]
                else:
                    dp_table[d][k][0] = max(dp_table[d-1][k][0], dp_table[d-1][k][1] + prices[d])
                    dp_table[d][k][1] = max(dp_table[d-1][k][1], dp_table[d-1][k-1][0] - prices[d])
        
        return dp_table[days-1][max_k][0]
    
# 優化空間複雜度
# 直接列出 k = 1, k = 2的情況
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i10, dp_i11 = 0, float('-inf')
        dp_i20, dp_i21 = 0, float('-inf')

        for d in range(len(prices)):
            for k in range(2, 0, -1):
                dp_i20 = max(dp_i20, dp_i21 + prices[d])
                dp_i21 = max(dp_i21, dp_i10 - prices[d])
                dp_i10 = max(dp_i10, dp_i11 + prices[d])
                dp_i11 = max(dp_i11, -prices[d])

        return dp_i20