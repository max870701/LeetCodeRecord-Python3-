class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        self.dp = [-1 for _ in range(self.n)]
        return self.f(0)
    
    # 返回由 i 位置開始decode的方法數
    def f(self, i):
        # Base case
        if i == self.n:
            return 1
        # 查表
        if self.dp[i] != -1:
            return self.dp[i]
        
        if self.s[i] == '0':
            return 0
        # 以下 self.s[i] != '0'
        # i 位置單獨轉化
        self.dp[i] = self.f(i+1) * (9 if self.s[i] == '*' else 1)
        # i i+1 位置一起轉化
        if i + 1 < self.n:
            if self.s[i] != '*':
                if self.s[i+1] != '*':
                    if int(self.s[i] + self.s[i+1]) <= 26:
                        self.dp[i] += self.f(i+2)
                else:
                    if self.s[i] == '1':
                        self.dp[i] += 9 * self.f(i+2)
                    elif self.s[i] == '2':
                        self.dp[i] += 6 * self.f(i+2)
            else: # self.s[i] == '*'
                if self.s[i+1] != '*':
                    if self.s[i+1] <= '6':
                        self.dp[i] += 2 * self.f(i+2)
                    else:
                        self.dp[i] += self.f(i+2)
                else:
                    self.dp[i] += 15 * self.f(i+2)
        
        self.dp[i] %= 1000000007

        return self.dp[i]


class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                # i 位置單獨轉化
                dp[i] = dp[i+1] * (9 if s[i] == '*' else 1)
                # i i+1 位置一起轉化
                if i + 1 < n:
                    if s[i] != '*':
                        if s[i+1] != '*':
                            if int(s[i] + s[i+1]) <= 26:
                                dp[i] += dp[i+2]
                        else:
                            if s[i] == '1':
                                dp[i] += 9 * dp[i+2]
                            elif s[i] == '2':
                                dp[i] += 6 * dp[i+2]
                    else: # s[i] == '*'
                        if s[i+1] != '*':
                            if s[i+1] <= '6':
                                dp[i] += 2 * dp[i+2]
                            else:
                                dp[i] += dp[i+2]
                        else:
                            dp[i] += 15 * dp[i+2]
                
                dp[i] %= 1000000007

        return dp[0]