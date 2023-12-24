class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        dp_table = [[0] * 2 for _ in range(days)]
        
        for d in range(days):
            # 第一天
            if d == 0:
                dp_table[0][0] = 0
                # 假設在買入時扣手續費
                dp_table[0][1] = -prices[d] - fee
            else:
                dp_table[d][0] = max(dp_table[d-1][0], dp_table[d-1][1] + prices[d])
                dp_table[d][1] = max(dp_table[d-1][1], dp_table[d-1][0] - prices[d] - fee)
        
        return dp_table[days-1][0]
    
# 空間複雜度優化class Solution:
def maxProfit(self, prices: List[int], fee: int) -> int:
    days = len(prices)
    # dp[-1][0], dp[-1][1]
    dp_i_0, dp_i_1 = 0, float('-inf')
    
    for d in range(days):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[d])
        dp_i_1 = max(dp_i_1, tmp - prices[d] - fee)
    
    return dp_i_0