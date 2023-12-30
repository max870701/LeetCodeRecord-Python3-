class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UF(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            # 若兩點原本已經連通，則產生環，生成不了樹
            if uf.connected(u, v):
                return False
            # 不產生環，將兩者連通
            uf.union(u, v)
        # 要保證最後只生成一顆樹，即只有一個連通分量
        return uf.count == 1
    
class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

class Solution2:
    def build(self, n):
        self.father = [i for i in range(n)]
        self.cnt = n

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
            self.cnt -= 1

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.build(n)
        for edge in edges:
            if self.isSameSet(edge[0], edge[1]): # 在相同集合中進行連通會形成環
                return False
            self.union(edge[0], edge[1])

        return self.cnt == 1