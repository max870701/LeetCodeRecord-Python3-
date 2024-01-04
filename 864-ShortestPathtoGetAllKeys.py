class Solution:
    def build(self, grid):
        row, col = len(grid), len(grid[0])
        char_grid = [list(s) for s in grid]
        max_key = 6
        queue = [[None] * 3 for _ in range(row * col * (1 << max_key))]
        l = r = key = 0
        for i in range(row):
            for j in range(col):
                # 起點
                if char_grid[i][j] == '@':
                    queue[r] = i, j, 0
                    r += 1
                # 目標 key 的狀態
                if ord('a') <= ord(char_grid[i][j]) <= ord('f'):
                    key |= (1 << (ord(char_grid[i][j])-ord('a')))
        
        visited = [[[False] * key for _ in range(col)] for _ in range(row)]

        return (char_grid, visited, queue, l, r, row, col, key)


    def shortestPathAllKeys(self, grid: List[str]) -> int:
        grid, visited, queue, l, r, row, col, key = self.build(grid)
        moves = [-1, 0, 1, 0, -1]
        level = 1
        while l < r:
            # level Size
            size = r - l
            for _ in range(size):
                x, y, status = queue[l]
                l += 1
                for i in range(4):
                    nx, ny = x + moves[i], y + moves[i+1]
                    nstatus = status
                    # 越界或是遇到障礙
                    if (not 0 <= nx < row) or (not 0 <= ny < col) or (grid[nx][ny] == '#'): continue
                    # 是鎖，又沒有對應的鑰匙
                    if (ord('A') <= ord(grid[nx][ny]) <= ord('F')) and (nstatus & (1 << (ord(grid[nx][ny]) - ord('A')))) == 0: continue
                    # 是某一把鑰匙
                    if ord('a') <= ord(grid[nx][ny]) <= ord('f'):
                        nstatus |= 1 << (ord(grid[nx][ny]) - ord('a'))
                    # 若達到目標key狀態
                    if nstatus == key: return level
                    # 若沒訪問過
                    if not visited[nx][ny][nstatus]:
                        visited[nx][ny][nstatus] = True
                        queue[r] = [nx, ny, nstatus]
                        r += 1
            level += 1

        return -1