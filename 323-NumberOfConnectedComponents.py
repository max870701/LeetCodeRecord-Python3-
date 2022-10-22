class Solution(object):
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