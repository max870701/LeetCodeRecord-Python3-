class Solution(object):
    def buildGraph(self, numCourses, prerequisites):
        # 圖中共有 numCourses 個節點
        # 構建鄰接表
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            # 添加一條從 from 指向 to 的有向邊
            # 邊的方向是「被依賴」關係，即修完課程 from 才能修 to
            fr, to = edge[1], edge[0]
            graph[fr].append(to)
        return graph

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 記錄一次遞歸堆棧中的節點
        self.onPath = [False for _ in range(numCourses)]
        # 記錄遍歷過的節點，防止走回頭路
        self.visited = [False for _ in range(numCourses)]
        # 記錄圖中是否有環
        self.hasCycle = False
        graph = self.buildGraph(numCourses, prerequisites)
        # 遍歷圖中所有節點
        for i in range(numCourses):
            self.traverse(graph, i)
        # 只要沒有循環依賴，即可以完成所有課程
        return not self.hasCycle
    
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
        self.onPath[s] = False

# Python3
from queue import Queue
class Solution:
    def buildGraph(self, numCourses, prerequisites):
        # 圖中共有 numCourses 個節點
        # 構建鄰接表
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            # 添加一條從 from 指向 to 的有向邊
            # 邊的方向是「被依賴」關係，即修完課程 from 才能修 to
            fr, to = edge[1], edge[0]
            graph[fr].append(to)
        return graph

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # BFS 解法
        # 構建圖，有向邊代表「被依賴」關係
        graph = self.buildGraph(numCourses, prerequisites)
        # 構建入度數組
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            fr, to = edge[1], edge[0]
            indegree[to] += 1
        # 根據入度初始化隊列中的節點
        q = Queue()
        for i in range(numCourses):
            # 節點 i 沒有入度，即沒有依賴的節點
            # 可作為拓墣排序的起點，加入隊列
            if indegree[i] == 0:
                q.put(i)
        # 記錄遍歷的節點個數
        count = 0
        # BFS
        while not q.empty():
            # 彈出節點 cur，並將他指向的節點入度減少1
            cur = q.get()
            count += 1
            for next in graph[cur]:
                indegree[next] -= 1
                # 如果入度變為 0，說明 next 依賴的節點都已被遍歷
                if indegree[next] == 0:
                    q.put(next)
        # 如果所有節點都被遍歷過，說明不成環
        return count == numCourses

class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [False] * numCourses
        self.hasCycle = False
        self.onPath = [False] * numCourses
        # 建圖
        self.graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            self.graph[edge[1]].append(edge[0])
        # dfs
        for node in range(numCourses):
            if not self.visited[node]:
                self.dfs(node)

        return not self.hasCycle
    
    def dfs(self, node):
        if self.onPath[node]:
            self.hasCycle = True
        if self.hasCycle or self.visited[node]:
            return
    
        self.visited[node] = True       
        self.onPath[node] = True
        for n_node in self.graph[node]:
            self.dfs(n_node)
        self.onPath[node] = False


class Solution3:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建圖
        # 入度表
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for edge in prerequisites:
            from_course, to_course = edge[1], edge[0]
            graph[from_course].append(to_course)
            indegree[to_course] += 1
        # 拓墣排序
        # 入隊列
        queue = []
        l, r = 0, 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                r += 1
        while l < r:
            cur = queue.pop()
            l += 1
            for n_node in graph[cur]:
                indegree[n_node] -= 1
                if indegree[n_node] == 0:
                    queue.append(n_node)
                    r += 1
        # 若拓墣排序後，存在 indegree 大於 0 的點，則代表存在環
        for i in range(numCourses):
            if indegree[i] != 0:
                return False
        return True