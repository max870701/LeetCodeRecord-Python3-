class Solution:
    def __init__(self):
        maxN = 31
        self.father = list(range(maxN))
        self.sets = 0

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pairs = n // 2
        self.build(pairs)
        for i in range(0, n, 2):
            self.union(row[i] // 2, row[i+1] // 2)
        return pairs - self.sets
    
    def build(self, m: int):
        self.father[:m] = [i for i in range(m)]
        self.sets = m
    
    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]
        
    def union(self, a, b):
        a_f = self.find(a)
        b_f = self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            self.sets -= 1