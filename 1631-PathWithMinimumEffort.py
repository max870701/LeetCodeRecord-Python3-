import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        # Deinfition: effortTo[i][j] is the minimum of effort from (0, 0) to (i, j)
        # Initialize the dp table
        effortTo = [[float('inf')] * n for _ in range(m)]
        # Base Case
        effortTo[0][0] = 0
        # Priority Queue
        # Deinfition: State [x, ,y, effort_from_start]
        pq = []
        heapq.heappush(pq, (0, [0, 0, 0]))
        while pq:
            cur_state = heapq.heappop(pq)[1]
            cur_x, cur_y, cur_effort_from_start = cur_state[0], cur_state[1], cur_state[2]
            # Return cur_effort_from_start if reach the end point
            if cur_x == m - 1 and cur_y == n - 1:
                return cur_effort_from_start
            if effortTo[cur_x][cur_y] < cur_effort_from_start:
                continue
            # Push (cur_x, cur_y) into the Priority Queue
            for neighbor in self.adj(heights, cur_x, cur_y):
                next_x, next_y = neighbor[0], neighbor[1]
                # Calculate the effort from (cur_x, cur_y) to (next_x, next_y)
                effort_to_next_node = max(effortTo[cur_x][cur_y], abs(heights[cur_x][cur_y] - heights[next_x][next_y]))
                # Update dp table
                if effort_to_next_node < effortTo[next_x][next_y]:
                    effortTo[next_x][next_y] = effort_to_next_node
                    heapq.heappush(pq, (effort_to_next_node, [next_x, next_y, effort_to_next_node]))
        # If there is no result
        return -1 

    def adj(self, matrix:List[List[int]], x:int, y:int) -> List[List[int]]:
        # directions
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        # Store adjacent nodes
        neighbors = []
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            # Check if the index is over the boundary
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            neighbors.append([nx, ny])

        return neighbors


from heapq import *
class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        distance = [[float('inf')] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
        # 初始化
        distance[0][0] = 0
        heap = []
        # [cost, row, col]
        heappush(heap, [0, 0, 0])
        # dijkstra
        moves = [-1, 0, 1, 0, -1]
        while heap:
            cost, x, y = heappop(heap)
            # 是否訪問過
            if visited[x][y]: continue
            # 到達右下角
            if x == row-1 and y == col-1: return cost
            # 上下左右移動
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + moves[i], y + moves[i+1]
                if (0 <= nx < row) and (0 <= ny < col) and (not visited[nx][ny]):
                    ncost = max(cost, abs(heights[x][y] - heights[nx][ny]))
                    if ncost < distance[nx][ny]:
                        distance[nx][ny] = ncost
                        heappush(heap, [ncost, nx, ny])

        return -1