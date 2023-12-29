class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # 圖為 favorite
        # 入度表
        n = len(favorite)
        indegree = [0] * n
        for i in range(n):
            indegree[favorite[i]] += 1
        # 入隊列
        queue = []
        l, r = 0, 0
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                r += 1
        # 拓墣排序推消息
        # deeps[i]: 不包括 i 在內，i 之前的最長鏈長度
        deeps = [0] * n
        while l < r:
            cur = queue.pop()
            l += 1
            fav = favorite[cur]
            deeps[fav] = max(deeps[fav], deeps[cur] + 1)
            indegree[fav] -= 1
            if indegree[fav] == 0:
                queue.append(fav)
                r += 1
        # 消除所有 indegree 為0的，只剩下環
        # 情況1: 小環 k=2，計算 兩個小環+各自延伸
        sumSmallRings = 0
        # 情況2: 大環 k>2，只計算最大環數
        bigRings = 0
        for i in range(n):
            if indegree[i] != 0:
                indegree[i] = 0
                ringSize = 1
                fav = favorite[i]
                while i != fav:
                    indegree[fav] = 0
                    ringSize += 1
                    fav = favorite[fav]
                # 判斷環種類
                if ringSize == 2:
                    sumSmallRings += 2 + deeps[i] + deeps[favorite[i]]
                if ringSize > 2:
                    bigRings = max(bigRings, ringSize)
        
        return max(sumSmallRings, bigRings)