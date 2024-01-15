# 遞歸 + 備忘錄
class Solution:
    def __init__(self):
        self.zeros = 0
        self.ones = 0

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.k = len(strs)
        self.dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(self.k)]
        return self.f(strs, 0, m, n)

    # strs[i...] 自由選擇，希望 0 的數量不超過 m ，且 1 的數量不超過 n
    # 返回最多能選多少個字串
    def f(self, strs, i, m, n):
        # base case
        if i == self.k:
            return 0
        # 搜索紀錄
        if self.dp[i][m][n] != -1:
            return self.dp[i][m][n]
        # 不使用當前 strs[i] 的字符串
        ans1 = self.f(strs, i+1, m, n)
        # 使用當前 strs[i] 的字符串
        ans2 = 0
        self.cntOnesAndZeros(strs[i])
        if self.zeros <= m and self.ones <= n:
            ans2 = 1 + self.f(strs, i+1, m - self.zeros, n - self.ones)
        
        self.dp[i][m][n] = max(ans1, ans2)
        return self.dp[i][m][n]

    # 計算一個字符串中的 0 和 1 數量
    def cntOnesAndZeros(self, s):
        self.zeros = 0
        self.ones = 0
        for char in s:
            if char == '0':
                self.zeros += 1
            else:
                self.ones += 1

# 嚴格位置依賴
class Solution2:
    def __init__(self):
        self.zeros = 0
        self.ones = 0

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        # strs[i...] 自由選擇，希望 0 的數量不超過 m ，且 1 的數量不超過 n，最多能選多少個字串
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(k+1)]
        # dp[len] 層全為 0
        for i in range(k-1, -1, -1):
            self.cntOnesAndZeros(strs[i])
            for z in range(m+1):
                for o in range(n+1):
                    # 不使用當前 strs[i]
                    ans1 = dp[i+1][z][o]
                    # 使用當前 strs[i]
                    ans2 = 0
                    if self.zeros <= z and self.ones <= o:
                        ans2 = 1 + dp[i+1][z - self.zeros][o - self.ones]
                    
                    dp[i][z][o] = max(ans1, ans2)

        return dp[0][m][n]

    # 計算一個字符串中的 0 和 1 數量
    def cntOnesAndZeros(self, s):
        self.zeros = 0
        self.ones = 0
        for char in s:
            if char == '0':
                self.zeros += 1
            else:
                self.ones += 1


# 嚴格位置依賴 + 空間壓縮
class Solution:
    def __init__(self):
        self.zeros = 0
        self.ones = 0

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # strs[i...] 自由選擇，希望 0 的數量不超過 m ，且 1 的數量不超過 n，最多能選多少個字串
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[len] 層全為 0
        for s in strs:
            self.cntOnesAndZeros(s)
            # z > self.zeros 且 o > self.ones 才有可能進行更新。
            # 否則維持原樣
            for z in range(m, self.zeros-1, -1):
                for o in range(n, self.ones-1, -1):
                    dp[z][o] = max(dp[z][o], 1 + dp[z - self.zeros][o - self.ones])

        return dp[m][n]

    # 計算一個字符串中的 0 和 1 數量
    def cntOnesAndZeros(self, s):
        self.zeros = 0
        self.ones = 0
        for char in s:
            if char == '0':
                self.zeros += 1
            else:
                self.ones += 1