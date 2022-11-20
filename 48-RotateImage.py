class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i + 1, length): #上三角部分
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            self.reverse(row)
    
    def reverse(self, array):
        """
        :type array: List[int]
        :rtype: None
        """
        # left, right pointer
        l, r = 0, len(array) - 1
        while l < r:
            array[r], array[l] = array[l], array[r]
            l += 1
            r -= 1
            