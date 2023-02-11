class Solution(object):
    def buildGraph(self, n, dislikes):
        # 圖節點編號為 1 開始到 n
        graph = [[] for _ in range(n+1)]
        for edge in dislikes:
            v = edge[1]
            w = edge[0]
            # 無向圖 == 雙向圖
            graph[v].append(w)
            graph[w].append(v)
        return graph

    def traverse(self, graph, v):
        if self.judge == False: return
        self.visited[v] = True
        for w in graph[v]:
            if not self.visited[w]:
                self.color[w] = not self.color[v]
                self.traverse(graph, w)
            else:
                if self.color[w] == self.color[v]:
                    self.judge = False
                    return

    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        self.judge = True
        self.color = [False for _ in range(n+1)]
        self.visited = [False for _ in range(n+1)]
        graph = self.buildGraph(n, dislikes)
        # 遍歷所有節點
        for v in range(1, n+1):
            if not self.visited[v]:
                self.traverse(graph, v)

        return self.judge