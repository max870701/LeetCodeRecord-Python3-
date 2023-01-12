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