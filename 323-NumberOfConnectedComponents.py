class Solution1(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if not seen[i]: # not connected
                count += 1
                seen[i] = True
                self.dfs(i=i, graph=graph, seen=seen)

        return count

    def dfs(self, i, graph, seen):
        for j in graph[i]:
            if not seen[j]:
                seen[j] = True
                self.dfs(j, graph, seen)

class Solution2(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UF(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.count

# Union Find 並查集
class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return
        
        self.parent[rootQ] = rootP
        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 