class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # Max number of stops is 1001
        d = Difference(nums=[0 for _ in range(1001)])
        for trip in trips:
            # Passenger got on the vehicle at the trip[1] stop
            # Passenger got off the vehicle at the trip[2] stop
            d.increment(start=trip[1],
                        end=trip[2] - 1,
                        val=trip[0]
                        )
        
        res = d.result()
        for n in res:
            if capacity < n:
                return False
        return True

class Difference(object):
    def __init__(self, nums):
        self.diff = nums
        # In general situation
        # self.diff = [nums[0]]
        # for i in range(1, len(nums)):
        #     self.diff += [nums[i] - nums[i-1]]
    
    def increment(self, start, end, val):
        self.diff[start] += val
        if end + 1 < len(self.diff):
            self.diff[end + 1] -= val
    
    # Re-construct the number array
    def result(self):
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res += [res[i - 1] + self.diff[i]]
        return res