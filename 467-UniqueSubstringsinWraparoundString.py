class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        s_num = [ord(c) - ord('a') for c in s]
        # dp[0]: s中必須以'a'做為結尾的子串，最大延伸長度是多少，延伸須根據base串的規則
        dp = [0] * 26
        dp[s_num[0]] = 1
        length = 1
        for i in range(1, n):
            pre, cur = s_num[i-1], s_num[i]
            if (pre == 25 and cur == 0) or (pre == cur - 1):
                length += 1
            else:
                length = 1

            dp[cur] = max(dp[cur], length)
        
        return sum(dp)