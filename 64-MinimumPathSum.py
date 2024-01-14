# 記憶化搜索(自頂置底)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        self.grid = grid
        self.dp = [[-1 for _ in range(col)] for _ in range(row)]
        return self.f(row - 1, col - 1)

    # 從 (0, 0) 到 (i, j) 的最小路徑和
    def f(self, i, j):
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if i == 0 and j == 0:
            self.dp[i][j] = self.grid[i][j]
        else:
            up = float('inf')
            left = float('inf')
            if i - 1 >= 0: # up
                up = self.f(i-1, j)
            if j - 1 >= 0: # left
                left = self.f(i, j-1)
            
            self.dp[i][j] = self.grid[i][j] + min(up, left)

        return self.dp[i][j]

# 嚴格位置依賴
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[-1 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[row-1][col-1]

# 嚴格位置依賴 + 空間壓縮
class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [-1 for _ in range(col)]
        dp[0] = grid[0][0]
        # 初始化
        for j in range(1, col):
            dp[j] = dp[j-1] + grid[0][j]
        # 迭代更新
        for i in range(1, row):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, col):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[col-1]