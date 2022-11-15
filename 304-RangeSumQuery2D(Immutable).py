class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        # preSum matrix (m+1) * (n+1)
        self.preSum = [[0] * (n+1) for i in range(m+1)]
        #self.preSum = [[0] * (n+1)] * (m+1) There is an issue in shallow copy in Python
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                self.preSum[row][col] = matrix[row-1][col-1] + self.preSum[row-1][col] + self.preSum[row][col-1] - self.preSum[row-1][col-1]
        print(self.preSum)
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)