class Solution:
    def build(self, n):
        self.father = [i for i in range(n)]

    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]

    def isSameSet(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a_f, b_f = self.find(a), self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])

        m = len(edgeList)
        k = len(queries)

        questions = [q + [i] for i, q in enumerate(queries)]
        questions.sort(key=lambda x: x[2])

        self.build(n)

        ans = [False] * k
        # i 為問題編號
        # j 為邊的編號
        j = 0
        for i in range(k):
            # 先將小於 questions 中限制的距離的 edge 全部連通
            while j < m and edgeList[j][2] < questions[i][2]:
                self.union(edgeList[j][0], edgeList[j][1])
                j += 1
            # 再進行查詢 questions[i] 中的兩節點是否連通(即小於距離門檻)，再將boolean答案填入對應的索引下
            ans[questions[i][3]] = self.isSameSet(questions[i][0], questions[i][1])

        return ans