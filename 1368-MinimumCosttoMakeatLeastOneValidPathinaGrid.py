from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # 建立 distance 二維數組，初始化為整數最大值
        distance = [[float('inf')] * col for _ in range(row)]
        distance[0][0] = 0
        # 雙端隊列初始化，放座標
        dq = deque([[0, 0]])
        # 遍歷
        # 右:1、左:2、下:3、上:4
        moves = [(), (0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(dq):
            # 彈出最左邊
            x, y = dq.popleft()
            if x == row-1 and y == col-1:
                return distance[x][y]
            for i in range(1, 5):
                n_x, n_y = x + moves[i][0], y + moves[i][1]
                weight = 0 if i == grid[x][y] else 1
                # 更新條件
                if (0 <= n_x < row) and (0 <= n_y < col) and (distance[x][y] + weight < distance[n_x][n_y]):
                    distance[n_x][n_y] = distance[x][y] + weight
                    # 若 weight 為 0，入隊頭
                    if weight == 0:
                        dq.appendleft([n_x, n_y])
                    # 若 weight 為 1，入隊尾
                    else:
                        dq.append([n_x, n_y])
        
        return -1