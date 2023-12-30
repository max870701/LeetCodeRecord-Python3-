class Solution:
    def build(self, n):
        self.father = [i for i in range(n+1)]
        self.edges = []
        self.cnt = 0

    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]
    
    def union(self, a, b):
        a_f, b_f = self.find(a), self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            return True
        else:
            return False

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        self.build(n)
        # 水源為 0，計算水源到所有點的成本（即 wells 成本）
        for i in range(n):
            self.edges.append([0, i+1, wells[i]])
        
        # 各個點之間修建 pipes 的成本
        cnt = n
        for pipe in pipes:
            self.edges.append(pipe)
            cnt += 1
        # Kruska 最小生成樹
        self.edges.sort(key=lambda x: x[2])
        ans = 0
        for i in range(cnt):
            if self.union(self.edges[i][0], self.edges[i][1]):
                ans += self.edges[i][2]
        
        return ans