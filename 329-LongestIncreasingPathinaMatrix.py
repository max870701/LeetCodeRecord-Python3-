class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.row, self.col = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        ans = 0
        for i in range(self.row):
            for j in range(self.col):
                ans = max(ans, self.f(matrix, i, j))
        
        return ans 
    
    # 從 (i, j) 出發，能走出來多長的遞增路徑，返回最長長度
    def f(self, matrix: List[List[int]], i: int, j: int) -> int:
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        next = 0
        origin = matrix[i][j]
        # 上
        if i-1 >= 0 and matrix[i-1][j] > origin:
            next = max(next, self.f(matrix, i-1, j))
        # 下
        if i+1 < self.row and matrix[i+1][j] > origin:
            next = max(next, self.f(matrix, i+1, j))
        # 左
        if j-1 >= 0 and matrix[i][j-1] > origin:
            next = max(next, self.f(matrix, i, j-1))
        # 右
        if j + 1 < self.col and matrix[i][j+1] > origin:
            next = max(next, self.f(matrix, i, j+1))

        self.dp[i][j] = 1 + next
        return 1 + next