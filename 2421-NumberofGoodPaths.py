class Solution:
    def __init__(self):
        MAXN = 30001
        self.father = list(range(MAXN))
        self.maxcnt = list(range(MAXN))
    
    def build(self, n):
        self.father[:n] = [i for i in range(n)]
        self.maxcnt[:n] = [1] * n

    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]

    def union(self, a, b, vals):
        a_f, b_f = self.find(a), self.find(b)
        a_f_val, b_f_val = vals[a_f], vals[b_f]
        path = 0
        if a_f_val < b_f_val:
            self.father[a_f] = b_f
        elif b_f_val < a_f_val:
            self.father[b_f] = a_f
        else: # good path
            path = self.maxcnt[a_f] * self.maxcnt[b_f]
            self.father[a_f] = b_f
            self.maxcnt[b_f] += self.maxcnt[a_f]
        return path

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        self.build(n)
        ans = n
        # 排序
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))
        # 遍歷合併
        for edge in edges:
            ans += self.union(edge[0], edge[1], vals)
        return ans