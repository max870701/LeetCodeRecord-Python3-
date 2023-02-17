class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # 每座城市相當於圖中的節點，連通城市的成本相當於邊的權重
        # 求連通城市的最小成本，即是最小生成樹的權重之和
        # 編號從 1 開始
        uf = UF(n+1)
        # key為成本，由小到大排序
        connections.sort(key=lambda x: x[2])
        # 記錄最小生成樹的權重之和
        mst = 0
        for edge in connections:
            u, v = edge[0], edge[1]
            weight = edge[2]
            # 若這條會產生環，則不能加入 mst
            if uf.connected(u, v):
                continue
            mst += weight
            uf.union(u, v)
        # 保證所有節點都連通
        # 按理說 uf.count == 1 說明所有節點連通
        # 但因為節點 0 沒有被使用, 所以 0 會額外佔用一個連通分量
        return mst if uf.count == 2 else -1


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