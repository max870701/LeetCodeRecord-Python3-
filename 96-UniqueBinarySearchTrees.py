class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 建立備忘綠
        self.memo = [[0] * (n+1) for _ in range(n+1)]
        return self.count(1, n)


    def count(self, lo, hi):
        """
        計算閉區間 [lo, hi] 組成的 BST 個數
        """
        # base case, 空節點
        if lo > hi:
            return 1
        # 查找備忘錄
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]
        res = 0
        # 窮舉
        for i in range(lo, hi+1):
            left = self.count(lo, i-1)
            right = self.count(i+1, hi)
            res += left * right
        # 存入備忘錄
        self.memo[lo][hi] = res
        return res
