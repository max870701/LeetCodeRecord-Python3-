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

from queue import Queue
class Solution2(object):
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
        # BFS 解法
        # 構建圖，有向邊代表「被依賴」關係
        graph = self.buildGraph(numCourses, prerequisites)
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            fr, to = edge[1], edge[0]
            indegree[to] += 1
        
        q = Queue()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.put(i)
        
        res = [0 for _ in range(numCourses)]
        count = 0
        while not q.empty():
            cur = q.get()
            res[count] = cur
            count += 1
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.put(next)
        if count != numCourses:
            return []
        return res    
    
class Solution3:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建圖（鄰接表、入度表）
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            from_node, to_node = edge[1], edge[0]
            graph[from_node].append(to_node)
            indegree[to_node] += 1
        # 隊列
        queue = list(range(numCourses))
        l = 0
        r = 0
        # indegree 為 0 的 node 先入隊
        for node in range(numCourses):
            if indegree[node] == 0:
                queue[r] = node
                r += 1
        # 刪除入度為 0 的點對其他點入度的影響
        cnt = 0
        while l < r:
            cur_node = queue[l]
            l += 1
            cnt += 1
            for neighbor in graph[cur_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue[r] = neighbor
                    r += 1
        
        return queue if cnt == numCourses else []