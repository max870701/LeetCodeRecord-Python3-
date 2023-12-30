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
    

class Solution2:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 建圖：鄰接表
        self.graph = [[] for _ in range(n+1)]
        for dislike in dislikes:
            n1, n2 = dislike[0], dislike[1]
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)
        # 二分圖判定
        self.judge = True
        self.visited = [False] * (n+1)
        self.color = [False] * (n+1)
        for node in range(1, n):
            if not self.visited[node]:
                self.dfs(node)

        return self.judge
    
    def dfs(self, node):
        if not self.judge: return

        self.visited[node] = True
        for n_node in self.graph[node]:
            if not self.visited[n_node]:
                self.color[n_node] = not self.color[node]
                self.dfs(n_node)
            else:
                if self.color[n_node] == self.color[node]:
                    self.judge = False
                    return