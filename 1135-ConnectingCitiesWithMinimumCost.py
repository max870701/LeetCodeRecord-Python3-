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
    

import heapq
class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = self.buildGraph(n, connections)
        prim = Prim(graph)
        
        if not prim.allConnected():
            return -1
        return prim.weightSum
    
    def buildGraph(self, n, connections):
        # 圖中有 n 個節點，創建鄰接表
        graph = [[] for _ in range(n)]
        for edge in connections:
            # 題目編號為 1，做偏移
            u, v = edge[0] - 1, edge[1] - 1
            weight = edge[2]
            # 無向圖就是雙向圖
            graph[u].append((u, v, weight))
            graph[v].append((v, u, weight))
        return graph

class Prim(object):
    def __init__(self, graph):
        self.graph = graph
        n = len(graph)
        self.pq = []
        # Visited 數組功用
        self.inMST = [False for _ in range(n)]
        self.weightSum = 0
        # 隨便從一個節點開始分割，不妨從節點 0 開始
        self.inMST[0] = True
        self.cut(0)
        # 不斷進行分割，向最小生成樹中添加邊
        while self.pq:
            edge = heapq.heappop(self.pq)
            # 形式 (priority_order, (node1, node2, weight))
            to = edge[1][1]
            weight = edge[1][2]
            # 節點 to 已經在最小生成樹中，則跳過
            # 避免產生 Cycle
            if self.inMST[to]:
                continue
            # 將 edge 加入最小生成樹
            self.weightSum += weight
            self.inMST[to] = True
            self.cut(to)
    
    def cut(self, s):
        # 遍歷 s 的鄰邊
        for edge in self.graph[s]:
            # edge的終點
            to = edge[1]
            # 若相鄰接點 to 已經在最小生成樹中，跳過
            if self.inMST[to]:
                continue
            # 不在最小生成樹中，則加入優先級隊列(照權重)
            # heapq.heappush(heap, (priority order, value))
            heapq.heappush(self.pq, (edge[2], edge))

    def allConnected(self):
        # 判斷最小生成樹是否包含圖中所有節點
        for i in range(len(self.inMST)):
            if not self.inMST[i]:
                return False
        return True

class Solution2:
    def build(self, n):
        self.father = [i for i in range(n+1)]
    
    def find(self, e):
        if self.father[e] != e:
            self.father[e] = self.find(self.father[e])
        return self.father[e]
    
    def union(self, a, b):
        a_f, b_f = self.find(a), self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            return True
        else:
            return False

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        self.build(n)
        connections.sort(key=lambda x: x[2])
        ans = 0
        edgeCnt = 0
        for edge in connections:
            if self.union(edge[0], edge[1]):
                edgeCnt += 1
                ans += edge[2]
            if edgeCnt == n-1: break
        
        return ans if edgeCnt == n-1 else -1