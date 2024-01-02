from queue import PriorityQueue
# 優先級隊列（二叉堆）
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pq = PriorityQueue()
        row, col = len(heightMap), len(heightMap[0])
        visited = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # 邊界先入優先級隊列
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    # 水線高度, x座標, y座標
                    pq.put((heightMap[i][j], i, j))
                    visited[i][j] = True
        # 遍歷
        moves = [-1, 0, 1, 0, -1]
        ans = 0
        while not pq.empty():
            h, x, y = pq.get()
            ans += h - heightMap[x][y] # 最小為 0
            # 上下左右
            for i in range(4):
                n_x, n_y = x + moves[i], y + moves[i+1]
                if (0 <= n_x < row) and (0 <= n_y < col) and (not visited[n_x][n_y]):
                    n_h = heightMap[n_x][n_y]
                    visited[n_x][n_y] = True
                    pq.put((max(n_h, h), n_x, n_y))
        
        return ans
    

from heapq import *
# 堆
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        row, col = len(heightMap), len(heightMap[0])
        visited = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # 邊界先入優先級隊列
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    # 水線高度, x座標, y座標
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        # 遍歷
        moves = [-1, 0, 1, 0, -1]
        ans = 0
        while heap:
            h, x, y = heappop(heap)
            ans += h - heightMap[x][y] # 最小為 0
            # 上下左右
            for i in range(4):
                n_x, n_y = x + moves[i], y + moves[i+1]
                if (0 <= n_x < row) and (0 <= n_y < col) and (not visited[n_x][n_y]):
                    n_h = heightMap[n_x][n_y]
                    visited[n_x][n_y] = True
                    heappush(heap, (max(n_h, h), n_x, n_y))
        
        return ans