class Solution(object):
    def buildGraph(self, numCourses, prerequisites):
        # 圖中共有 numCourses 個節點
        # 構建鄰接表
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            # 添加一條從 from 指向 to 的有向邊
            # 邊的方向是「被依賴」關係，即修完課程 from 才能修 to
            # [ai, bi] 先修 bi 才修 ai
            fr, to = edge[1], edge[0]
            graph[fr].append(to)
        return graph

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.postorder = []
        self.hasCycle = False
        self.visited = [False for _ in range(numCourses)]
        self.onPath = [False for _ in range(numCourses)]
        graph = self.buildGraph(numCourses, prerequisites)
        # 遍歷圖
        for i in range(numCourses):
            self.traverse(graph, i)
        # 有環，返回空列表
        if self.hasCycle:
            return []
        # 逆後序遍歷結果，即為拓墣排序結果
        return self.postorder[::-1]
    
    def traverse(self, graph, s):
        # 重複，即出現環
        if self.onPath[s]:
            self.hasCycle = True
        # 剪枝
        if self.visited[s] or self.hasCycle:
            return
        # 前序
        self.visited[s] = True
        self.onPath[s] = True
        #
        for t in graph[s]:
            self.traverse(graph, t)
        # 後序
        self.postorder.append(s)
        self.onPath[s] = False