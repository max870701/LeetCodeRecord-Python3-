class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        self.size = len(nums)
        while i < self.size:
            triples = self.threeSum(nums, i+1, target - nums[i])
            for t in triples:
                res.append([nums[i]] + t)
            while (i < self.size - 1) and (nums[i] == nums[i+1]):
                i += 1
            i += 1
        return res          

    def threeSum(self, nums, start, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = start
        while i < self.size:
            tuples = self.twoSum(nums, i+1, target - nums[i])
            for t in tuples:
                res.append([nums[i]] + t)
            while i < self.size-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


    def twoSum(self, nums, start,  target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left, right = start, len(nums) - 1
        
        while left < right:
            sum_num = nums[left] + nums[right]
            left_num, right_num = nums[left], nums[right]
            if sum_num < target:
                while (left < right) and (nums[left] == left_num):
                    left += 1
            elif sum_num > target:
                while (left < right) and (nums[right] == right_num):
                    right -= 1
            else: # sum_num == target
                res.append([left_num, right_num])
                while (left < right) and (nums[left] == left_num):
                    left += 1
                while (left < right) and (nums[right] == right_num):
                    right -= 1
        return res