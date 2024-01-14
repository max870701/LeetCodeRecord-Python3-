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