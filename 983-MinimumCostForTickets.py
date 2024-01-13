class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs
        self.duration = (1, 7, 30)
        self.n = len(days)
        self.dp = [float('inf') for _ in range(self.n)]
        return self.f(0)

    # 從第i天開始，旅行的最少花費
    def f(self, i):
        # 越界後，花費為0
        if i == self.n:
            return 0
        # 檢查是否在 dp 數組中出現過
        if self.dp[i] != float('inf'):
            return self.dp[i]
        # 窮舉搜索 duration (1, 7, 30)
        j = i
        for d in range(3):
            while (j < self.n) and (self.days[i] + self.duration[d] > self.days[j]):
                j += 1
            self.dp[i] = min(self.dp[i], self.costs[d] + self.f(j))

        return self.dp[i]


    
class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        duration = (1, 7, 30)
        n = len(days)
        # 記錄從 i 位置到 n 的最小花費
        dp = [float('inf') for _ in range(n+1)]
        dp[n] = 0
        for i in range(n-1, -1, -1):
            j = i
            for k in range(3):
                while j < n and days[i] + duration[k] > days[j]:
                    j += 1
                dp[i] = min(dp[i], costs[k] + dp[j])
        
        return dp[0]