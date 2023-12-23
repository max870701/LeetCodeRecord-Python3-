class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ans = set()
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1:
                    self.path = ''
                    self.dfs(i, j, 6)
                    ans.add(self.path)

        return len(ans)
    
    # 若 (i, j) 為陸地則淹沒與其相連的陸地，並記錄遍歷順序（即島嶼形狀）
    def dfs(self, i, j, direction):
        # 索引越界
        if not (0 <= i < self.row) or not (0 <= j < self.col): return
        # 已經是海水
        if self.grid[i][j] == 0: return 
        # 淹沒
        self.grid[i][j] = 0
        # 前序記錄進入路徑
        self.path += str(direction) + ','
        # 上下左右
        self.dfs(i-1, j, 1)
        self.dfs(i+1, j, 2)
        self.dfs(i, j-1, 3)
        self.dfs(i, j+1, 4)
        # 後序記錄返回路徑
        self.path += str(-direction) + ','