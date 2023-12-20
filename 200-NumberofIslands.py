from queue import Queue
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        num = 0

        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == '1':
                    num += 1
                    self.bfs(i, j)
        return num

    # 搜尋上下左右的格子是否為1，若為1，則設置為0並且繼續進行bfs搜索
    def bfs(self, i, j):
        q = Queue()
        q.put((i, j))
        self.grid[i][j] = 0

        while not q.empty():
            s = q.qsize()
            for _ in range(s):
                coord = q.get()
                i, j = coord[0], coord[1]
                if i - 1 >= 0 and self.grid[i-1][j] == '1':
                    q.put((i-1, j))
                    self.grid[i-1][j] = '0' 
                if i + 1 < self.row and self.grid[i+1][j] == '1':
                    q.put((i+1, j))
                    self.grid[i+1][j] = '0'
                if j - 1 >= 0 and self.grid[i][j-1] == '1':
                    q.put((i, j-1))
                    self.grid[i][j-1] = '0'
                if j + 1 < self.col and self.grid[i][j+1] == '1':
                    q.put((i, j+1))
                    self.grid[i][j+1] = '0'    

    
    # 搜尋上下左右的格子是否為1，若為1，則設置為0並且繼續進行dfs搜索
    def dfs(self, i, j):
        # 若非 1 或是索引越界，則停下
        if (i < 0) or (i >= self.row) or (j < 0) or (j >= self.col) or (self.grid[i][j] != '1'):
            return
        # 設置為 0
        self.grid[i][j] = '0'
        # 若為1則向上下左右進行搜索
        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)

    # 優化過的 BFS
    def bfs2(self, i, j):
        q = Queue()
        q.put(i*self.col + j)
        self.grid[i][j] = 0

        while not q.empty():
            s = q.qsize()
            for _ in range(s):
                n = q.get()
                i, j = n // self.col, n % self.col
                if i - 1 >= 0 and self.grid[i-1][j] == '1':
                    q.put((i-1)*self.col + j)
                    self.grid[i-1][j] = '0' 
                if i + 1 < self.row and self.grid[i+1][j] == '1':
                    q.put((i+1)*self.col + j)
                    self.grid[i+1][j] = '0'
                if j - 1 >= 0 and self.grid[i][j-1] == '1':
                    q.put(i*self.col + (j-1))
                    self.grid[i][j-1] = '0'
                if j + 1 < self.col and self.grid[i][j+1] == '1':
                    q.put(i*self.col + (j+1))
                    self.grid[i][j+1] = '0'