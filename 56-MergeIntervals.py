class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        out = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= out[0][1]:
                out[-1][0] = min(out[-1][0], i[0])
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out

class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by the start position
        intervals.sort(key=lambda pos: pos[0])
        ans = [intervals[0]]

        # Iterate the intervals array and merge overlapped interval
        for start, end in intervals[1:]:
            prev_end = ans[-1][1]
            if start <= prev_end:
                ans[-1][1] = max(prev_end, end)
            else:
                ans.append([start, end])
        
        return ans