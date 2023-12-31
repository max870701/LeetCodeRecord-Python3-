class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = []
        visited = [[False] * col for _ in range(row)]
        l, r = 0, 0
        seas = 0
        # 入隊列
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    r += 1
                    visited[i][j] = True
                else:
                    seas += 1
        # 全是海洋或全是陸地
        if seas == 0 or seas == row * col: return -1
        # 層序遍歷
        level = 0
        moves = [-1, 0, 1, 0, -1]
        while l < r:
            level += 1
            # 同一層
            size = r - l
            for _ in range(size):
                cur_x, cur_y = queue[l]
                l += 1
                for i in range(4):
                    next_x, next_y = cur_x + moves[i], cur_y + moves[i+1]
                    if (0 <= next_x < row) and (0 <= next_y < col) and (not visited[next_x][next_y]):
                        visited[next_x][next_y] = True
                        queue.append([next_x, next_y])
                        r += 1
        
        return level - 1

    
from queue import Queue
class Solution2:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = Queue()
        visited = [[False] * col for _ in range(row)]
        seas = 0
        # 入隊列
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q.put([i, j])
                    visited[i][j] = True
                else:
                    seas += 1
        # 全是海洋或全是陸地
        if seas == 0 or seas == row * col: return -1
        # 層序遍歷
        level = 0
        moves = [-1, 0, 1, 0, -1]
        while not q.empty():
            level += 1
            size = q.qsize()
            for _ in range(size):
                x, y = q.get()
                for i in range(4):
                    n_x, n_y = x + moves[i], y + moves[i+1]
                    if (0 <= n_x < row) and (0 <= n_y < col) and (not visited[n_x][n_y]):
                        visited[n_x][n_y] = True
                        q.put([n_x, n_y])
        
        return level - 1