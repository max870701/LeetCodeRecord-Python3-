class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.dp = [[[-1 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
        self.n = n
        return self.f(row, column, k)

    # 從 (i, j) 出發，還剩下 k 步要走，返回最後在棋盤上的機率
    def f(self, i: int, j: int, k: int) -> float:
        # 越界，返回 0
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return 0
        # 查找dp表中是否有記錄
        if self.dp[i][j][k] != -1:
            return self.dp[i][j][k]
        # 計算生存機率
        ans = 0
        # 剩下 0 步，100% 存活
        if k == 0:
            ans = 1
        # 8 個方向查找一遍
        else:
            ans += self.f(i-2, j-1, k-1) / 8
            ans += self.f(i-2, j+1, k-1) / 8
            ans += self.f(i+2, j-1, k-1) / 8
            ans += self.f(i+2, j+1, k-1) / 8
            ans += self.f(i-1, j-2, k-1) / 8
            ans += self.f(i+1, j-2, k-1) / 8
            ans += self.f(i-1, j+2, k-1) / 8
            ans += self.f(i+1, j+2, k-1) / 8
        
        self.dp[i][j][k] = ans
        return ans