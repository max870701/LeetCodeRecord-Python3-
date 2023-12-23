class Solution:
    # 求被 water 包圍的 land 數量
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.row, self.col = len(grid), len(grid[0])
        self.grid = grid
        ans = 0
        # 先去掉上下左右四個邊的陸地
        for i in range(self.row): # 淹左右
            self.dfs(i, 0)
            self.dfs(i, self.col - 1)
        for j in range(self.col): # 淹上下
            self.dfs(0, j)
            self.dfs(self.row - 1, j)
        # 計算陸地數量
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 0:
                    ans += 1
                    self.dfs(i, j)

        return ans
    
    # 從 (i, j) 開始搜索，與之相鄰的陸地皆淹為海水
    def dfs(self, i, j):
        # 索引越界
        # if i < 0 or i >= self.row or j < 0 or j >= self.col: return
        if not (0 <= i < self.row) or not (0 <= j < self.col): return
        # 已經是海水
        if self.grid[i][j] == 1: return
        # 淹沒
        self.grid[i][j] = 1
        # 上、下、左、右
        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)