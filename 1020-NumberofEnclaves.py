class Solution:
    # 求不能靠邊的島嶼數量
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row, self.col = len(self.grid), len(self.grid[0])
        ans = 0
        # 先淹沒所有靠邊島嶼和與之連接的島嶼
        for i in range(self.row): # 淹左右
            self.dfs(i, 0)
            self.dfs(i, self.col-1)
        for j in range(self.col): # 淹上下
            self.dfs(0, j)
            self.dfs(self.row-1, j)
        # 計算島嶼數量
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1:
                    ans += 1

        return ans

    # 若 (i, j) 是島嶼，淹沒與之相連的所有島嶼
    def dfs(self, i, j):
        # 索引越界
        if not (0 <= i < self.row) or not (0<= j < self.col):return
        # 已經是海水
        if self.grid[i][j] == 0: return
        # 淹沒
        self.grid[i][j] = 0
        # 淹沒上下左右
        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)