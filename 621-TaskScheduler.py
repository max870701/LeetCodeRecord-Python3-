import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = Counter(tasks)
        max_heap = [-count for count in freq_dict.values()]
        heapq.heapify(max_heap)

        dq = deque() # (count, idleTime)
        cur_time = 0

        while max_heap or dq:
            cur_time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    dq.append((count, cur_time + n))

            if dq and dq[0][1] == cur_time:
                c, t = dq.popleft()
                heapq.heappush(max_heap, c)

        return cur_time


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = Counter(tasks)
        _, k = freq_dict.most_common(1)[0]

        p = 0
        for v in freq_dict.values():
            if v == k:
                p += 1
        
        return max((k-1)*(n+1)+p, len(tasks))