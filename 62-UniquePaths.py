class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Time Limit Exceeded in testcase
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths1(self, m, n):
        # Assume m is the number of rows, n is the number of columns
        # 0 to m-1, 0 to n-1
        count_matrix = [[1] * n for _ in range(m)]

        # Counting, but not includes the start position (0, 0)
        for col in range(1, n):
            for row in range(1, m):
                count_matrix[row][col] = count_matrix[row-1][col] + count_matrix[row][col-1]

        return count_matrix[m-1][n-1]

    def uniquePaths2(self, m, n):
        # A classical combinatorial problem
        # Let steps to through rows is v = m - 1
        # Let steps to through columns is h = n - 1
        # So the total steps we move from (0, 0) to (m-1, n-1) is v + h
        # If we already determine the orders of moving vertically,
        # and then the orders of moving horizontally will also be determined.
        # Hence, the problem can be simplified to
        # "How many ways one could choose v (or h) elements from (v+h) elements."
        # We apply the formula of combination to solve it.
        from math import factorial

        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
