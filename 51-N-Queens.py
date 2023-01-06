class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(board, row, col):
            # 判斷放置位置是否合法
            for i in range(row):
                for j in range(n):
                    # 正上方: j == col 
                    # 左上方: i - j == row - col
                    # 右上方: i + j == row + col
                    if board[i][j] == 'Q' and (j == col or i + j == row + col or i - j == row - col):
                        return False
            return True

        def backtrack(board, row):
            if row == n:
                cur_res = ["".join(row) for row in board]
                res.append(cur_res)
                return
            for col in range(n):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'

        res = []
        board = [['.'] * n for _ in range(n)]
        backtrack(board, 0)
        return res

    
    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(row, col, board):
            # 若該 column 或 左對角線 或 右對角線 上有皇后，則不合法
            if (col in col_hash) or ((row - col) in left_diag) or ((row + col) in right_diag):
                return False
            return True

        def backtrack(board, row):
            if row >= n:
                cur_res = [''.join(row) for row in board]
                res.append(cur_res)
                return
            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = 'Q'
                    col_hash.add(col)
                    left_diag.add(row - col)
                    right_diag.add(row + col)
                    backtrack(board, row+1)
                    board[row][col] = '.'
                    col_hash.remove(col)
                    left_diag.remove(row - col)
                    right_diag.remove(row + col)

        res = []
        board = [['.'] * n for _ in range(n)]
        # 列
        col_hash = set() 
        # 左對角線
        left_diag = set()
        # 右對角線
        right_diag = set()
        backtrack(board,0)
        return res