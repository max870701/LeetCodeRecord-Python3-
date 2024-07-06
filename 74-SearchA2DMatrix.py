class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 分別對 ROW 和 COL 進行二分搜索，時間複雜度為 O(log(m) + log(n))
        # 先確定找哪一 ROW，再對指定的 ROW 進行 COL 進行二分搜索
        # 注意此處是使用閉區間搜索
        top_row, bot_row = 0, len(matrix) - 1
        left_col, right_col = 0, len(matrix[0]) - 1

        while top_row < bot_row:
            mid_row = (top_row + bot_row) >> 1
            if matrix[mid_row][right_col] == target:
                return True
            elif matrix[mid_row][right_col] > target:
                bot_row = mid_row
            elif matrix[mid_row][right_col] < target:
                top_row = mid_row + 1
            
        target_row = top_row

        while left_col <= right_col:
            mid_col = (left_col + right_col) >> 1
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] > target:
                right_col = mid_col - 1
            elif matrix[target_row][mid_col] < target:
                left_col = mid_col + 1
        
        return False