class Solution(object):
    # 自頂向下，備忘綠優化
    def fib(self, n):
        self.memo = [0 for _ in range(n+1)]
        return self.helper(n)

    def helper(self, n):
        if n == 0 or n == 1:
            return n
        if self.memo[n] != 0:
            return self.memo[n]
        self.memo[n] = self.helper(n-1) + self.helper(n-2)
        return self.memo[n]
    # 自頂向下，暴力解法
    def fib1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        return self.fib1(n-1) + self.fib1(n-2)
    # 自底向上迭代，dp數組
    def fib2(self, n):
        if n == 0:
            return 0
        dp = [0 for _ in range(n+1)]
        # base case
        dp[0], dp[1] = 0, 1
        # 狀態轉移
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    # 自底向上迭代，空間優化
    def fib3(self, n):
        # base case
        if n == 0 or n == 1:
            return n
        # 遞推關係
        prev, curr = 0, 1
        for _ in range(2, n+1):
            s = prev + curr
            prev = curr
            curr = s
        return curr