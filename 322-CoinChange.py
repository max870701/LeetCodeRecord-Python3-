import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        <法一> 暴力遞歸解法(複雜度高，容易超時)
        ----------
        狀態:目標金額 amount
        選擇:coins數組中列出的所有硬幣面額
        函數的定義:湊出金額 amount,至少需要 coinChange(coins, amount) 枚硬幣
        Base Case: amount == 0 時，需要 0 枚硬幣; amount < 0 時，不可能湊出

        -> 備忘錄優化
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.memo = [-666 for _ in range(amount+1)]
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        if amount == 0: return 0
        if amount < 0: return -1
        # 查看備忘錄，防止重複計算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = sys.maxsize
        for coin in coins:
            # 計算子問題結果
            subProblem = self.dp(coins, amount - coin)
            # 子問題無解則跳過
            if subProblem == -1: continue
            # 在子問題中選擇最優解，然後加一
            res = min(res, subProblem + 1)
        # 將計算結果存入備忘綠
        self.memo[amount] = -1 if res == sys.maxsize else res
        return self.memo[amount]

    def coinChange1(self, coins, amount):
        """
        <法二> 自底向上迭代解法
        dp 數組的定義：湊出總金額 amount, 至少需要 dp[amount] 枚硬幣
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp數組全部初始化為特殊值 amount + 1
        dp = [amount+1 for _ in range(amount+1)]
        # Base Case
        dp[0] = 0
        # 遍歷所有狀態的所有取值
        for i in range(len(dp)):
            # 遍歷在求所有選擇的最小值
            for coin in coins:
                # 子問題無解，跳過
                if i - coin < 0: continue
                # 狀態轉移
                dp[i] = min(dp[i], 1 + dp[i - coin])
        # 看看金額 amount 能不能湊出來
        return -1 if dp[amount] == amount + 1 else dp[amount]