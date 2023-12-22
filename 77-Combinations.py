class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.track = []
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start, n, k):
        # base case
        if k == len(self.track):
            self.res.append(list(self.track))
            return
        # backtracking framework
        for i in range(start, n+1):
            # selecting
            self.track.append(i)
            # avoid duplicate
            self.backtrack(i+1, n, k)
            # withdraw selecting
            self.track.pop()

class Solution:
    # 返回 [1, n] 中 n 選 k 的組合
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.track = []
        self.backtrack(1, n, k)
        return self.ans    
    
    def backtrack(self, start, end, k):
        # Base case
        if len(self.track) == k:
            self.ans.append(self.track[:])
            return
        # 做選擇、遞歸多叉樹、撤銷選擇
        for i in range(start, end+1):
            self.track.append(i)
            self.backtrack(i+1, end, k)
            self.track.pop()