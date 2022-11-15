class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        d = Difference(nums=([0] * length)) 
        for update in updates:
            d.increment(start=update[0], end=update[1], val=update[2])
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
