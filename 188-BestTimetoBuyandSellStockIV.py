class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if not days: return 0
        if k > (days / 2):
            return self.maxProfitInf(prices)
        dp_table = [[[0] * 2 for _ in range(k+1)] for _ in range(days)]
        # k = 0 時的 base case
        for i in range(days):
            dp_table[i][0][0] = 0
            dp_table[i][0][1] = float('-inf')

        for i in range(days):
            for j in range(k, 0, -1):
                if i == 0:
                    dp_table[i][j][0] = 0
                    dp_table[i][j][1] = -prices[i]
                else:
                    dp_table[i][j][0] = max(dp_table[i-1][j][0], dp_table[i-1][j][1] + prices[i])
                    dp_table[i][j][1] = max(dp_table[i-1][j][1], dp_table[i-1][j-1][0] - prices[i])
        
        return dp_table[days-1][k][0]

    # 若 k 大於 prices 列表的一半長度，則代表 k 沒有限制 （因為一買一賣算一次 k）
    def maxProfitInf(self, prices):
        days = len(prices)
        dp_table = [[0] * 2 for _ in range(days)]
        
        for d in range(days):
            if d == 0:
                dp_table[0][0] = 0
                dp_table[0][1] = -prices[d]
            else:
                dp_table[d][0] = max(dp_table[d-1][0], dp_table[d-1][1] + prices[d])
                dp_table[d][1] = max(dp_table[d-1][1], dp_table[d-1][0] - prices[d])

        return dp_table[days-1][0]