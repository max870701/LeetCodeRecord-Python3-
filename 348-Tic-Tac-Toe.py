from collections import defaultdict

class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.size = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diag = 0
        self.antidiag = 0

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        sign = 1 if player == 1 else -1
        self.rows[row] += sign
        self.cols[col] += sign

        if (row == col):
            self.diag += sign
        if (row + col == self.size - 1):
            self.antidiag += sign
        
        if (abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(self.diag) == self.size or abs(self.antidiag) == self.size):
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)