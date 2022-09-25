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
