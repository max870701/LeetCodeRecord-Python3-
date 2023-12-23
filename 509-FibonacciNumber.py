class Solution:
    # 自頂向下，備忘綠優化，時間複雜度 O(n)
    def fib(self, n):
        self.memo = [0] * (n+1)
        return self.dp(n)

    def dp(self, n):
        # Base case
        if n == 0 or n == 1: return n
        # 檢查 memo
        if self.memo[n]: return self.memo[n]
        # 遞迴
        self.memo[n] = self.dp(n-1) + self.dp(n-2)
        return self.memo[n]
    
    # 自頂向下，暴力解法，時間複雜度 O(2 ^ n)
    def fib1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        return self.fib1(n-1) + self.fib1(n-2)
    
    # 自底向上迭代，dp table 數組
    def fib2(self, n: int) -> int:
        if n == 0: return 0
        dp_table = [0] * (n+1)
        # Base Definition
        dp_table[0], dp_table[1] = 0, 1
        # 遞迴定義式 (狀態轉移方程)
        for i in range(2, n+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
        return dp_table[n]
    
    # 自底向上迭代，空間優化
    def fib3(self, n):
        # base case
        if n == 0 or n == 1:
            return n
        # 遞推關係
        prev, cur = 0, 1
        for _ in range(2, n+1):
            next = prev + cur
            prev, cur = cur, next
        return cur