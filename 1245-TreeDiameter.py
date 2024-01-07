class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        if n == 0: return 0
        # 鄰接表建圖
        self.graph = [[] for _ in range(n+1)]
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        # 搜索最大直徑（邊）
        self.res = 0
        self.visited = [False for _ in range(n+1)]
        self.maxDepth(edges[0][0])
        return self.res

    # 給定任意節點作為根節點，返回最大直徑
    def maxDepth(self, root):
        if self.visited[root]: return 0
        self.visited[root] = True

        first_depth, second_depth = 0, 0
        for child in self.graph[root]:
            child_depth = self.maxDepth(child)
            if child_depth > first_depth:
                first_depth, second_depth = child_depth, first_depth
            elif child_depth > second_depth:
                second_depth = child_depth
        # 後序
        diameter = first_depth + second_depth
        self.res = max(self.res, diameter)

        return 1 + first_depth