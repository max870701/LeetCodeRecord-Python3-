class Solution:
    # 給定 grid, 返回最大面積的島嶼
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        maxArea = 0
        curArea = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1:
                    curArea = self.dfs(i, j)
                maxArea = max(maxArea, curArea)

        return maxArea

    # 若 (i, j) 是陸地，返回計算連通的面積(注意：計算後需要淹沒島嶼避免重複計算)
    def dfs(self, i, j):
        # 索引越界
        if not (0 <= i < self.row) or not (0 <= j < self.col): return 0
        # 已經是海水
        if self.grid[i][j] == 0: return 0
        # 淹沒
        self.grid[i][j] = 0
        # 上下左右查找，返回面積
        up = self.dfs(i-1, j)
        down = self.dfs(i+1, j)
        left = self.dfs(i, j-1)
        right = self.dfs(i, j+1)

        return 1 + up + down + left + right
    

class Solution2:
    # 給定 grid, 返回最大面積的島嶼
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        maxArea = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(i, j))

        return maxArea

    # 若 (i, j) 是陸地，返回計算連通的面積(注意：計算後需要淹沒島嶼避免重複計算)
    def dfs(self, i, j):
        # 索引越界
        if not (0 <= i < self.row) or not (0 <= j < self.col): return 0
        # 已經是海水
        if self.grid[i][j] == 0: return 0
        # 淹沒
        self.grid[i][j] = 0
        # 上下左右查找，返回面積
        return 1 + self.dfs(i-1, j) + self.dfs(i+1, j) + self.dfs(i, j-1) + self.dfs(i, j+1)