class Solution:
    # 返回 grid2 在 grid1 中子島嶼的數量
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        self.grid1 = grid1
        self.grid2 = grid2
        self.row, self.col = len(grid2), len(grid2[0])

        # 先排除 grid2 有陸地但 grid2 是海水的情況
        for i in range(self.row):
            for j in range(self.col):
                if self.grid2[i][j] == 1 and self.grid1[i][j] == 0:
                    # 代表 grid2[i][j] 相連的那整塊陸地必不是 grid1 的子島嶼，因次進行淹沒  
                    self.dfs(i, j)
        # 此時 grid2 中有陸地的島嶼皆為 grid1 的子島嶼
        for i in range(self.row):
            for j in range(self.col):
                if self.grid2[i][j] == 1:
                    ans += 1
                    self.dfs(i, j)

        return ans

    # 若 (i, j) 為陸地，則淹沒相連的陸地
    def dfs(self, i, j):
        # 索引越界
        if not (0 <= i < self.row) or not (0 <= j < self.col): return
        # 已經是海水
        if self.grid2[i][j] == 0: return
        # 淹沒
        self.grid2[i][j] = 0
        # 上下左右查找
        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)