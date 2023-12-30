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


import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        graph = self.buildGraph(n, points)
        return Prim(graph).weightSum
    
    def buildGraph(self, n, points):
        graph = [[] for _ in range(n)]
        # 生成所有邊及權重  
        for i in range(n):
            for j in range(i+1, n):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                weight = abs(xi - xj) + abs(yi - yj)
                # 用 points 中的索引表示座標點
                graph[i].append((i, j, weight))
                graph[j].append((j, i, weight))
        
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
        self.father = [i for i in range(n)]
    
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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        p_len = len(points)
        self.build(p_len)
        # 構建 edges
        edges = []
        for i in range(p_len):
            for j in range(i+1, p_len):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                edges.append([
                    i,
                    j,
                    abs(xi - xj) + abs(yi - yj)
                ])
        # 依照權重排序
        edges.sort(key=lambda x: x[2])
        # 最小生成樹 Kruskal
        ans = 0
        edgeCnt = 0
        for edge in edges:
            if self.union(edge[0], edge[1]):
                edgeCnt += 1
                ans += edge[2]
        
        return ans