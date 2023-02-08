class Solution(object):
    def traverse(self, graph, s, path):
        # 添加節點 s 到路徑
        path.append(s)
        n = len(graph)
        if s == n - 1:
            # 到達終點 -> 找到一條起點到終點的路徑
            self.res.append(list(path))
        # 遞歸遍歷每個相鄰節點
        for v in graph[s]:
            self.traverse(graph, v, path)
        # 從路徑移出節點 s
        path.pop()            

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # 有向無環圖，不需要 visited
        self.res = []
        # path 用於維護遞歸過程中經過的路徑
        path = []
        self.traverse(graph, 0, path)
        return self.res