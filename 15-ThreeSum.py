class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    
    def twoSum(self, nums, i, res):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            sumThree = nums[i] + nums[lo] + nums[hi]
            if sumThree < 0:
                lo += 1
            elif sumThree > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1