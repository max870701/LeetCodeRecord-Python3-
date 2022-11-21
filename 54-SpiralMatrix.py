class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        upper_bound = left_bound = 0
        lower_bound = m - 1
        right_bound = n - 1
        res = []
        # The matrix size is m * n
        while len(res) < m * n:
            # Step1: start at upper_bound
            if upper_bound <= lower_bound:
                for col in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][col])
                # Move down the upper bound
                upper_bound += 1
            # Step2: start at right bound
            if left_bound <= right_bound:
                for row in range(upper_bound, lower_bound + 1):
                    res.append(matrix[row][right_bound])
                # Move left the right bound
                right_bound -= 1
            # Step3: start at lower bound
            if upper_bound <= lower_bound:
                for col in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][col])
                # Move up the lower bound
                lower_bound -= 1
            # Step4: start at left bound    
            if left_bound <= right_bound:
                for row in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[row][left_bound])
                # Mover right the left bound
                left_bound += 1
        
        return res