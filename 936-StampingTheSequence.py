class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s_len, t_len = len(stamp), len(target)
        # 入度表
        indegree = [s_len] * (t_len - s_len + 1)
        # 隊列
        queue = list(range(t_len - s_len + 1))
        # 建圖
        graph = [[] for _ in range(t_len)]
        l, r = 0, 0
        for i in range(t_len - s_len + 1):
            for j in range(s_len):
                if target[i+j] == stamp[j]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue[r] = i
                        r += 1
                else: # 錯誤位置影響的開頭下標
                    graph[i+j].append(i)

        # 同一個位置取消錯誤不要重複計算
        vistied = [False] * t_len
        # 收集 queue 彈出的節點
        path = list(range(t_len - s_len + 1))
        size = 0
        while l < r:
            cur = queue[l]
            l += 1
            path[size] = cur
            size += 1
            for i in range(s_len):
                if not vistied[cur+i]:
                    vistied[cur+i] = True
                    for n_node in graph[cur+i]:
                        indegree[n_node] -= 1
                        if indegree[n_node] == 0:
                            queue[r] = n_node
                            r += 1
        
        if size != t_len - s_len + 1:
            return []

        return path[::-1]