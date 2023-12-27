class Solution:
    def __init__(self):
        MAXN = 301
        self.father = list(range(MAXN))
        self.sets = 0
    
    def build(self, n):
        self.father[:n] = [i for i in range(n)]
        self.sets = n

    def numSimilarGroups(self, strs: List[str]) -> int:
        strs_cnt = len(strs)
        strs_len = len(strs[0])

        self.build(strs_cnt)

        for i in range(strs_cnt):
            for j in range(i+1, strs_cnt):

                if self.find(i) != self.find(j):

                    diff = 0
                    k = 0
                    while diff < 3 and k < strs_len:
                        if strs[i][k] != strs[j][k]:
                            diff += 1
                        k += 1

                    if diff == 0 or diff == 2:
                        self.union(i, j)
                        
        return self.sets

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