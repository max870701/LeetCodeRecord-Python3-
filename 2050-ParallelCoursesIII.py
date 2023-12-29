class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n+1)]
        indegree = [0] * (n+1)
        # 建圖、更新indegree
        for edge in relations:
            from_course, to_course = edge[0], edge[1]
            graph[from_course].append(to_course)
            indegree[to_course] += 1
        # indegree 為 0 者入隊列
        queue = []
        l, r = 0, 0
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
                r += 1
        # 拓墣排序
        costs = [0] * (n+1)
        ans = 0
        while l < r:
            cur = queue[l]
            l += 1
            costs[cur] += time[cur-1]
            ans = max(ans, costs[cur])
            for n_course in graph[cur]:
                costs[n_course] = max(costs[n_course], costs[cur])
                indegree[n_course] -= 1
                if indegree[n_course] == 0:
                    queue.append(n_course)
                    r += 1
        return ans