# 自頂向底 + 記憶化搜索
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.f(s, 0, n-1, dp)
    
    # 定義：返回 s[L...R] 的最長回文子序列長度
    def f(self, s: str, l: int, r: int, dp: List[List[int]]) -> int:
        if dp[l][r] != -1:
            return dp[l][r]
        # base case 1
        if l == r:
            return 1
        # base case 2
        if l+1 == r:
            return 2 if s[l] == s[r] else 1
        # 情況1
        if s[l] == s[r]:
            dp[l][r] = 2 + self.f(s, l+1, r-1, dp)
        # 情況2
        else:
            dp[l][r] = max(self.f(s, l, r-1, dp), self.f(s, l+1, r, dp))
        
        return dp[l][r]
    
# 嚴格位置依賴，自底向頂
class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(n-1, -1, -1):
            dp[l][l] = 1
            if l+1 < n:
                dp[l][l+1] = 2 if s[l] == s[l+1] else 1
            for r in range(l+2, n):
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l+1][r-1]
                else:
                    dp[l][r] = max(dp[l][r-1], dp[l+1][r])
        
        return dp[0][n-1]
    
# 嚴格位置依賴 + 空間壓縮
class Solution3:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for l in range(n-1, -1, -1):
            dp[l] = 1
            left_down = 0

            if l+1 < n:
                left_down = dp[l+1]
                dp[l+1] = 2 if s[l] == s[l+1] else 1

            for r in range(l+2, n):
                tmp = dp[r]
                if s[l] == s[r]:
                    dp[r] = 2 + left_down
                else:
                    dp[r] = max(dp[r-1], dp[r])
                left_down = tmp
        
        return dp[n-1]