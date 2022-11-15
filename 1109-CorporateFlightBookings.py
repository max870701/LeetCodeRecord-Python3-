class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        d = Difference(nums=[0 for _ in range(n)]) 
        for booking in bookings:
            d.increment(start=booking[0] - 1,
                        end=booking[1] - 1,
                        val=booking[2])
        return d.result()

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