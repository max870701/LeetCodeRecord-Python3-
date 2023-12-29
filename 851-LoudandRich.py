class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        q_len = len(quiet)
        # 鄰接表
        graph = [[] for _ in range(q_len)]
        # 入度表
        indegree = [0] * q_len
        # 建圖
        for edge in richer:
            from_node, to_node = edge[0], edge[1]
            graph[from_node].append(to_node)
            indegree[to_node] += 1
        # 入度為 0 的點入隊列
        queue = []
        l, r = 0, 0
        for i in range(q_len):
            if indegree[i] == 0:
                queue.append(i)
                r += 1
        # 初始化 ans
        ans = [i for i in range(q_len)]
        # 拓墣排序: 推送消息並更新 ans
        while l < r:
            cur_node = queue[l]
            l += 1
            for n_node in graph[cur_node]:
                if quiet[ans[cur_node]] < quiet[ans[n_node]]:
                    ans[n_node] = ans[cur_node]
                indegree[n_node] -= 1
                if indegree[n_node] == 0:
                    queue.append(n_node)
                    r += 1
        
        return ans