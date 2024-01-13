class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        # 記錄子串必須以 i 位置的字符結尾的情況下，往左最多能推多遠能讓整體有效
        dp = [0 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                p = i - dp[i-1] - 1
                if p >= 0 and s[p] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[p-1] if p-1 >= 0 else 0)

                ans = max(ans, dp[i])

        return ans 