class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 記錄醜數
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        # 乘上 2, 3, 5 推得
        i2 = i3 = i5 = 1
        for i in range(2, n+1):
            a = dp[i2] * 2
            b = dp[i3] * 3
            c = dp[i5] * 5

            cur = min(a, b, c)

            if cur == a:
                i2 += 1
            if cur == b:
                i3 += 1
            if cur == c:
                i5 += 1

            dp[i] = cur
        
        return dp[n]