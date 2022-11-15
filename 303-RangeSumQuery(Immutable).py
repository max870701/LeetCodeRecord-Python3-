class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0]
        #for i in range(1, len(nums) + 1):
        #    self.preSum += [self.preSum[i-1] + nums[i-1]]
        for num in nums:
            self.preSum += [self.preSum[-1] + num]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right+1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)