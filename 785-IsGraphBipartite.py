class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 記錄圖是否符合二分圖性質
        self.judge = True
        # 記錄圖中節點的顏色，False 和 True 代表兩種不同顏色
        n = len(graph)
        self.color = [False for _ in range(n)]
        # 記錄途中節點是否被訪問過
        self.visited = [False for _ in range(n)]
        # 圖不一定連通，可能存在多個子圖
        # 所以要把每個節點都做為起點進行一次遍歷
        # 若發現任何一個子圖不是二分圖，整個圖都不算二分圖
        for v in range(n):
            if not self.visited[v]:
                self.traverse(graph, v)

        return self.judge
    
    def traverse(self, graph, v):
        # DFS遍歷
        # 如果確定不是二分圖，結束traverse
        if self.judge == False: return
        # 記錄訪問過的節點
        self.visited[v] = True
        # 訪問相鄰節點
        for w in graph[v]:
            # 沒訪問過
            if not self.visited[w]:
                self.color[w] = not self.color[v]
                self.traverse(graph, w)
            # 訪問過
            else:
                # 若 w 和 v 顏色相同，則不是二分圖
                if self.color[w] == self.color[v]:
                    self.judge = False
                    return

from Queue import Queue
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 記錄圖是否符合二分圖性質
        self.judge = True
        # 記錄圖中節點的顏色，False 和 True 代表兩種不同顏色
        n = len(graph)
        self.color = [False for _ in range(n)]
        # 記錄途中節點是否被訪問過
        self.visited = [False for _ in range(n)]
        # 圖不一定連通，可能存在多個子圖
        # 所以要把每個節點都做為起點進行一次遍歷
        # 若發現任何一個子圖不是二分圖，整個圖都不算二分圖
        for v in range(n):
            if not self.visited[v]:
                self.bfs(graph, v)

        return self.judge
    
    def bfs(self, graph, start):
        # BFS遍歷框架
        q = Queue()
        self.visited[start] = True
        q.put(start)
        # 遍歷
        while not q.empty() and self.judge:
            v = q.get()
            # 從 v 節點向周圍擴散
            for w in graph[v]:
                if not self.visited[w]:
                    self.color[w] = not self.color[v]
                    self.visited[w] = True
                    q.put(w)
                else:
                    if self.color[w] == self.color[v]:
                        self.judge = False
                        return