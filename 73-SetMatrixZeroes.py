class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        columns_0, rows_0 = set(), set()
        row_len = len(matrix[0])
        i = 0
        
        for m in matrix:
            if 0 in set(m):
                rows_0.add(i)
                for j, n in enumerate(m):
                    if n == 0:
                        columns_0.add(j)
            i += 1

        for r, rows in enumerate(matrix):
            if r in rows_0:
                matrix[r] = [0] * row_len
            else:
                for s in columns_0:
                    rows[s] = 0
                    
        return matrix