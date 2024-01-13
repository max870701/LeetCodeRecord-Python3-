# 自頂向下
class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        self.dp = [-1 for _ in range(self.n)]
        return self.f(0)

    # 從 i 位置開始的答案數 
    def f(self, i):
        # Base case：一種有效方法數
        if i == self.n:
            return 1
        # 搜尋 dp table中是否出現過
        if self.dp[i] != -1:
            return self.dp[i]
        # 搜索
        if self.s[i] == '0':
            self.dp[i] = 0
        else:
            # self.s[i] != '0'
            # 轉 1 個字符串的情況
            self.dp[i] = self.f(i+1)
            # 轉 2 個字符串的情況
            if (i + 1 < self.n) and (int(self.s[i] + self.s[i+1]) <= 26):
                self.dp[i] += self.f(i+2)
        
        return self.dp[i]
    
# 嚴格位置依賴的動態規劃
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for _ in range(n+1)]
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i + 1 < n and int(s[i] + s[i+1]) <= 26:
                    dp[i] += dp[i+2]
        
        return dp[0]

# 嚴格位置依賴的動態規劃 + 空間壓縮
class Solution3:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[0...n]
        next = 1
        # dp[n+1] 不存在
        nextnext = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = next
                if i + 1 < n and int(s[i] + s[i+1]) <= 26:
                    cur += nextnext
            nextnext = next
            next = cur
        
        return cur