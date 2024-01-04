from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        distance = [[float('inf')] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
        # 初始化
        distance[0][0] = 0
        heap = []
        # [cost, row, col]
        heappush(heap, [grid[0][0], 0, 0])
        # 遍歷
        moves = [-1, 0, 1, 0, -1]
        while heap:
            cost, x, y = heappop(heap)
            if visited[x][y]: continue
            if x == row-1 and y == col-1: return cost
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + moves[i], y + moves[i+1]
                if (0 <= nx < row) and (0 <= ny < col) and (not visited[nx][ny]):
                    ncost = max(cost, grid[nx][ny])
                    if ncost < distance[nx][ny]:
                        distance[nx][ny] = ncost
                        heappush(heap, [ncost, nx, ny])
        return -1