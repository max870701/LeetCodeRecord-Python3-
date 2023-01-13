class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 備忘錄
        memo = dict()
        # 定義: dp(i, j) 返回 s1[0..i] 和 s2[o..j] 的最小編輯距離
        def dp(i, j):
            # base case
            if i == -1: return j + 1
            if j == -1: return i + 1
            # Lookup memo
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]: # 啥都不做
                memo[(i, j)] = dp(i-1, j-1)
            else: # 窮舉所有可能
                memo[(i, j)] = min(
                    dp(i, j-1) + 1,  # 插入
                    dp(i-1, j) + 1,  # 刪除
                    dp(i-1, j-1) + 1 # 替換
                )
            return memo[(i, j)]
        # i, j 初始化指向最後一個索引   
        return dp(len(word1)-1, len(word2)-1)

    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # 定義: dp[i][j] 返回 s1[0..i-1] 和 s2[o..j-1] 的最小編輯距離
        dp = [[0] * (n+1) for _ in range(m+1)]
        # base case
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j 
        # 自底向上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1, # 刪除
                        min(
                            dp[i][j-1] + 1, # 插入
                            dp[i-1][j-1] + 1 # 替換
                        )
                    )
        return dp[m][n]