class Solution:
    def __init__(self):
        MAXN = 1001
        self.father = list(range(MAXN))
    
    def build(self, m):
        self.father[:m] = [i for i in range(m)] # 石頭編號作為 Union Find 的元素
        self.sets = m
        self.rowFirst = dict()  # key: 某 row , value: 第一次遇到的石頭編號
        self.colFirst = dict()  # key: 某 col , value: 第一次遇到的石頭編號
    
    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]

    def union(self, a, b):
        a_f, b_f = self.find(a), self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            self.sets -= 1

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.build(n)
        for i in range(n):
            x, y = stones[i][0], stones[i][1]
            if x not in self.rowFirst:
                self.rowFirst.setdefault(x, i)
            else:
                self.union(i, self.rowFirst[x])
            if y not in self.colFirst:
                self.colFirst.setdefault(y, i)
            else:
                self.union(i, self.colFirst[y])
            
        return n - self.sets