# https://leetcode.cn/problems/DFPeFJ/description/
from heapq import *
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        n = len(charge)
        # 鄰接表建無向圖
        graph = [[] for _ in range(n)]
        for path in paths:
            from_city, to_city, s = path
            graph[from_city].append((to_city, s))
            graph[to_city].append((from_city, s))
        # 初始化狀態 (城市，到達該城市的電量) 圖上的點
        distance = [[float('inf')] * (cnt+1) for _ in range(n)]
        distance[start][0] = 0 
        # 訪問記錄
        visited = [[False] * (cnt+1) for _ in range(n)]
        # 小根堆
        heap = []
        # (花費時間，當前點，來到當前點所花費電量)
        heappush(heap, (0, start, 0))
        while heap:
            cost, cur, power = heappop(heap)
            if visited[cur][power]: continue
            if cur == end: return cost
            visited[cur][power] = True
            # 充一格電
            if power < cnt:
                if not visited[cur][power+1] and cost + charge[cur] < distance[cur][power+1]:
                    distance[cur][power+1] = cost + charge[cur]
                    heappush(heap, (cost+charge[cur], cur, power+1))
            # 前往下一座城市
            for edge in graph[cur]:
                nextCity = edge[0]
                nextPower = power - edge[1]
                nextCost = cost + edge[1]
                if nextPower >= 0 and not visited[nextCity][nextPower] and nextCost < distance[nextCity][nextPower]:
                    distance[nextCity][nextPower] = nextCost
                    heappush(heap, (nextCost, nextCity, nextPower))
        
        return -1