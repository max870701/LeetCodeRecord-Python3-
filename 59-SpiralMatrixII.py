class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # n square matrix
        res = [[0] * n for _ in range(n)]
        upper_bound = left_bound = 0
        lower_bound = right_bound = n - 1
        # start at 1
        num = 1
        # The matrix size is m * n
        while num <= n ** 2:
            # Step1: start at upper_bound
            if upper_bound <= lower_bound:
                for col in range(left_bound, right_bound + 1):
                    res[upper_bound][col] = num
                    num += 1
                # Move down the upper bound
                upper_bound += 1
            # Step2: start at right bound
            if left_bound <= right_bound:
                for row in range(upper_bound, lower_bound + 1):
                    res[row][right_bound] = num
                    num += 1
                # Move left the right bound
                right_bound -= 1
            # Step3: start at lower bound
            if upper_bound <= lower_bound:
                for col in range(right_bound, left_bound - 1, -1):
                    res[lower_bound][col] = num
                    num += 1
                # Move up the lower bound
                lower_bound -= 1
            # Step4: start at left bound    
            if left_bound <= right_bound:
                for row in range(lower_bound, upper_bound - 1, -1):
                    res[row][left_bound] = num
                    num += 1
                # Mover right the left bound
                left_bound += 1
        
        return res