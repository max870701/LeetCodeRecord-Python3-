# 嚴格位置依賴
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.mod = 1000000007
        m = len(group)
        self.m = m
        self.profit, self.group = profit, group
        # dp[m][n][profit]
        # dp[m][][] 到頭為 0
        self.dp = [[[-1 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(m)]
        return self.f(0, n, minProfit)

    def f(self, i: int, worker: int, res_profit: int) -> int:
        """
        i: 來到 i 工作
        worker: 員工額度還有 worker 人，若 worker <= 0 說明無法繼續工作
        profit: 利潤還有 profit 才能達標，若 profit <= 0 說明之前的選擇已經讓利潤達標了
        return: 方案數量
        """
        # Base case
        if worker <= 0:
            return 1 if res_profit == 0 else 0
        if i == self.m:
            return 1 if res_profit == 0 else 0
        
        if self.dp[i][worker][res_profit] != -1:
            return self.dp[i][worker][res_profit]
        # 不要當前工作
        plan1 = self.f(i+1, worker, res_profit)
        # 要當前工作
        plan2 = 0   
        if self.group[i] <= worker: # 人力夠才做
            plan2 = self.f(i+1, worker - self.group[i], max(0, res_profit - self.profit[i]))
        
        self.dp[i][worker][res_profit] = (plan1 + plan2) % self.mod

        return self.dp[i][worker][res_profit]

# 嚴格位置依賴 + 空間壓縮
class Solution2:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 1000000007
        m = len(group)
        # dp[worker][profit]
        dp = [[0 for _ in range(minProfit+1)] for _ in range(n+1)]
        # i == m 越界位置
        for w in range(n+1):
            # base case 
            dp[w][0] = 1
        # 從高層往低層填寫
        for i in range(m-1, -1, -1):
            for w in range(n, -1, -1):
                for p in range(minProfit, -1, -1):
                    # 不選當前工作
                    plan1 = dp[w][p]
                    # 選當前工作
                    plan2 = dp[w - group[i]][max(0, p - profit[i])] if group[i] <= w else 0
                    # 計算方案數
                    dp[w][p] = (plan1 + plan2) % MOD

        return dp[n][minProfit] 