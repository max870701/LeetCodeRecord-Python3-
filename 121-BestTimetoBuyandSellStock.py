class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # k = 1 固定，狀態變量為 i 天和 持倉狀態
        days = len(prices)
        # 記錄最大收益
        dp_table = [[0 for _ in range(2)] for _ in range(days)]
        
        for d in range(days):
            if d == 0: # Base case
                # 第 1 天無持倉 -> 收益 0
                dp_table[0][0] = 0
                # 第 1 天持倉(buy) -> 收益 -prices[0]
                dp_table[0][1] = -prices[0]
            # 第 d 天無持倉
            # 情況 1: 第 d-1 天也無持倉
            # 情況 2: 第 d-1 有持倉，今日sell
            dp_table[d][0] = max(dp_table[d-1][0], dp_table[d-1][1] + prices[d])
            # 第 d 天有持倉
            # 情況 1: 第 d-1 天也有持倉
            # 情況 2: 第 d-1 無持倉，今日buy
            dp_table[d][1] = max(dp_table[d-1][1], -prices[d])
        
        return dp_table[days-1][0]
    
# 空間優化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # k = 1 固定，狀態變量為 i 天和 持倉狀態
        days = len(prices)
        # Base case
        dp_i_0, dp_i_1 = 0, float('-inf')
        
        for d in range(days):
            # 第 d 天無持倉
            # 情況 1: 第 d-1 天也無持倉
            # 情況 2: 第 d-1 有持倉，今日sell
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[d])
            # 第 d 天有持倉
            # 情況 1: 第 d-1 天也有持倉
            # 情況 2: 第 d-1 無持倉，今日buy
            dp_i_1 = max(dp_i_1, -prices[d])
        
        return dp_i_0