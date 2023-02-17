class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        # 生成所有邊及權重
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                # 用座標點在 points 中的索引表示座標點
                edges.append(list([i, j, abs(xi - xj) + abs(yi - yj)]))
        # 將邊按照權重從小到大排序
        edges.sort(key=lambda x: x[2])
        # Kruskal Algorithm
        mst = 0
        uf = UF(n)
        for edge in edges:
            u, v = edge[0], edge[1]
            weight = edge[2]
            # 會產生環，不加入mst，繼續遍歷下一個
            if uf.connected(u, v):
                continue
            # 不產生環，加入mst
            mst += weight
            uf.union(u, v)
        return mst
            

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