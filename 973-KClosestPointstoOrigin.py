import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_dist(point):
            return math.sqrt(pow(point[0], 2) + pow(point[1], 2))
        
        res = []
        heapq.heapify(res)

        for point in points:
            tmp_dist = cal_dist(point)
            if len(res) < k:
                heapq.heappush(res, (-tmp_dist, point))
            elif tmp_dist < -res[0][0]:
                heapq.heappush(res, (-tmp_dist, point))
                heapq.heappop(res)
        
        return [t[1] for t in res]
                
