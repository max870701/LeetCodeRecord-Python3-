from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # 0-1 BFS
        row, col = len(grid), len(grid[0])
        # 建立 distance 二維記錄表，初始化為最大值
        distance = [[float('inf')] * col for _ in range(row)]
        # 移動
        moves = [-1, 0, 1, 0, -1]
        # 層序遍歷
        distance[0][0] = 0
        # 雙端隊列，記錄座標
        dq = deque([[0, 0]])
        while len(dq) > 0:
            # 彈出左側座標
            x, y = dq.popleft()
            # 到達右下角，返回結果
            if x == row-1 and y == col-1:
                return distance[x][y]
            # 上下左右移動並更新 distance
            for i in range(4):
                n_x, n_y = x + moves[i], y + moves[i+1]
                # 更新條件
                # 1) 索引沒越界
                # 2) distance[x][y] + grid[n_x][n_y] 的距離小於 distance[n_x][n_y] 當前距離
                if (0 <= n_x < row) and (0 <= n_y < col) and (distance[n_x][n_y] > distance[x][y] + grid[n_x][n_y]):
                    distance[n_x][n_y] = distance[x][y] + grid[n_x][n_y]
                    # 路徑為 0 則加入雙端隊列頭部
                    if grid[n_x][n_y] == 0:
                        dq.appendleft([n_x, n_y])
                    # 路徑為 1 則加入雙端隊列尾部
                    else: # grid[n_x][n_y] == 1
                        dq.append([n_x, n_y])
        
        return -1