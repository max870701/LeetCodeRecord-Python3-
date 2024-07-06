# 無法用DP
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.row, self.col = len(board), len(board[0])
        self.word_len = len(word)

        for i in range(self.row):
            for j in range(self.col):
                if self.f(i, j, 0):
                    return True
                
        return False

    # 從 (i, j) 出發，來到word[k]，請問後續能不能把word走出來word[k...]
    def f(self, i: int, j: int, k: int) -> bool:
        if k == self.word_len:
            return True
        if not (0 <= i < self.row and 0 <= j < self.col and self.board[i][j] == self.word[k]):
            return False
        
        tmp = self.board[i][j]
        self.board[i][j] = 0
        ans = self.f(i-1, j, k+1) or self.f(i+1, j, k+1) or self.f(i, j-1, k+1) or self.f(i, j+1, k+1)
        self.board[i][j] = tmp
        return ans

class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if (i < 0 or i == row or j < 0 or j == col or board[i][j] != word[k]):
                return False
            
            tmp = board[i][j]
            board[i][j] = "0"
            ans = find(i+1, j, k+1) or find(i-1, j, k+1) or find(i, j+1, k+1) or find(i, j-1, k+1)
            board[i][j] = tmp

            return ans
            
        # 從每一個點出發尋找
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if find(i, j, 0):
                    return True

        return False