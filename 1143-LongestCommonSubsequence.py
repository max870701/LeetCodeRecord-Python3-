# 記憶化搜索
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len, text2_len = len(text1), len(text2)
        self.dp = [[-1 for _ in range(text2_len + 1)] for _ in range(text1_len + 1)]
        return self.f(text1, text2, text1_len, text2_len)
    
    # 給定 t1[前綴長度為len1] 和 t2[前綴長度為len2]
    # 返回最長公共子序列長度
    def f(self, t1: str, t2: str, len1: int, len2: int) -> int:
        if len1 == 0 or len2 == 0:
            return 0
        if self.dp[len1][len2] != -1:
            return self.dp[len1][len2]

        if t1[len1-1] == t2[len2-1]:
            self.dp[len1][len2] = self.f(t1, t2, len1-1, len2-1) + 1
        else:
            self.dp[len1][len2] = max(self.f(t1, t2, len1-1, len2), self.f(t1, t2, len1, len2-1))

        return self.dp[len1][len2]
    
# 嚴格位置依賴(自底向上)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for len1 in range(1, n+1):
            for len2 in range(1, m+1):
                if text1[len1-1] == text2[len2-1]:
                    dp[len1][len2] = 1 + dp[len1-1][len2-1]
                else:
                    dp[len1][len2] = max(dp[len1-1][len2], dp[len1][len2-1])
        
        return dp[n][m]
    
# 嚴格位置依賴 + 空間壓縮
