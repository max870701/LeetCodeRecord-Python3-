from heapq import heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        meetings = [intervals[0][1]] # end time

        for start, end in intervals[1:]:
            if start >= meetings[0]:
                heappop(meetings)
            
            heappush(meetings, end)

        return len(meetings)

    
class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)
        
        return res