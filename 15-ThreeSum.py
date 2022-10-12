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
                self.twoSum2(nums, i, res)

        return res

    
    def twoSum1(self, nums, i, res):
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

    def twoSum2(self, nums, i, res):
        hashset = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in hashset:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            hashset.add(nums[j])
            j += 1