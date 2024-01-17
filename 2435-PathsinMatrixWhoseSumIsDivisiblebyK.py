# 記憶化搜索
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        self.mod = 1000000007
        self.row, self.col = len(grid), len(grid[0])
        self.grid = grid
        self.k = k
        # dp[row][col][k]
        self.dp = [[[-1 for _ in range(k)] for _ in range(self.col)] for _ in range(self.row)]
        return self.f(0, 0, 0)
    
    # 從 (i, j) 出發，最終走到右下角 (row-1, col-1)，有多少路徑累加和 %k 的餘數是 r
    def f(self, i: int, j: int, r: int) -> int:
        # 走到右下角，進行判斷
        if i == self.row - 1 and j == self.col - 1:
            return 1 if self.grid[i][j] % self.k == r else 0

        if self.dp[i][j][r] != -1:
            return self.dp[i][j][r]

        # 計算下之後路徑和所需餘數
        need = (self.k + r - (self.grid[i][j] % self.k)) % self.k
        ans = 0
        if i + 1 < self.row:
            ans = self.f(i+1, j, need)
        if j + 1 < self.col:
            ans = (ans + self.f(i, j+1, need)) % self.mod

        self.dp[i][j][r] = ans
        return ans
    
# 嚴格位置依賴
class Solution2:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        row, col = len(grid), len(grid[0])
        # dp[row][col][k] 厚度k
        dp = [[[0 for _ in range(k)] for _ in range(col)] for _ in range(row)]
        dp[row-1][col-1][grid[row-1][col-1] % k] = 1
        # 填 row - 1 行的所有格子
        for j in range(col-2, -1, -1):
            for r in range(k):
                dp[row-1][j][r] = dp[row-1][j+1][(k + r - (grid[row-1][j] % k)) % k]
        # 填 col - 1 列的所有格子
        for i in range(row-2, -1, -1):
            for r in range(k):
                dp[i][col-1][r] = dp[i+1][col-1][(k + r - (grid[i][col-1] % k)) % k]
        # 填剩下依賴右邊和下面的格子
        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                for r in range(k):
                    need = (k + r - (grid[i][j] % k)) % k
                    # 右
                    dp[i][j][r] = dp[i+1][j][need]
                    # 下
                    dp[i][j][r] = (dp[i][j][r] + dp[i][j+1][need]) % mod
        
        return dp[0][0][0]